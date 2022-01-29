"""project.jobs.emails"""
import os
import requests

from jobs import logger, jobs_path # pylint: disable=E0401

def get_message() -> str:
    '''retrieving the email message'''
    msg_path = os.environ.get('MESSAGE_PATH', 'res/email_message2.txt')
    msg_path = os.path.join(jobs_path, msg_path)
    if not os.path.isfile(msg_path):
        raise IOError(f'{msg_path} not found!')
    message= ''
    with open(msg_path, 'r', encoding='utf-8') as f_msg:
        message = f_msg.read()
    return message

def get_recipients(url):
    '''retrieving the registered email list'''
    try:
        res = requests.get(url)
    except requests.exceptions.RequestException as err:
        logger.error(str(err))
        return None
    email_list = []
    if res.status_code == 200:
        res = res.json()
        if res['count'] == 0:
            logger.warning('registered email list is empty!')
            return []
        for record in res['result']:
            email_list.append(record['email_address'])
    return email_list
