"""project.jobs.tasks"""
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from celery.schedules import crontab

from jobs import ( # pylint: disable=E0401
    celery_app,
    SMTP_HOST,
    SMTP_PORT,
    SMTP_ACCOUNT,
    SMTP_PASSWORD,
    logger
)

from jobs.emails import get_recipients, get_message # pylint: disable=E0401

@celery_app.task(bind=True)
def email_notification(self) -> None: # pylint: disable=W0613
    '''send email notification'''
    url = os.environ.get('WEB_SERVER_URL', 'http://localhost:8080')
    from_email = SMTP_ACCOUNT
    to_email   = get_recipients(f'{url}/api/v1/recipients/')
    subject    = "Happy New Week!!"
    message    = get_message()

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as smtp_server:
            smtp_server.login(SMTP_ACCOUNT, SMTP_PASSWORD)
            if 'Content-type: text/html' in message:
                smtp_server.sendmail(from_email, to_email, message)
            else:
                msg            = MIMEText(message, 'plain')
                msg['Subject'] = subject
                msg['From']    = from_email
                msg['To']      = ",".join(to_email)
                smtp_server.sendmail(from_email, to_email, msg.as_string())
    except smtplib.SMTPException as err:
        logger.error(str(err))
        return False
    return True

@celery_app.on_after_configure.connect
def send_weekly_notice(sender, **kwargs):  # pylint: disable=W0613
    '''add periodic task into the schedule'''
    sender.add_periodic_task(
        crontab(hour=7, minute='30', day_of_week=1),
        email_notification.s(),
    )
