"""project.jobs.__init__"""
import os
import logging
import yaml
from celery import Celery

jobs_path = os.path.abspath(os.path.dirname(__file__))

# Logging configuration
logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# loading smtp server configuration data
SMTP_HOST     = None
SMTP_PORT     = None
SMTP_ACCOUNT  = None
SMTP_PASSWORD = None
config_path = os.path.join(jobs_path, 'res/config.yml')
with open(config_path, 'r', encoding='utf-8') as fp:
    try:
        smtp_config = yaml.safe_load(fp)
    except yaml.YAMLError as yml_err:
        print(str(yml_err))
    else:
        SMTP_HOST     = smtp_config.get('smtp_host')
        SMTP_PORT     = smtp_config.get('smtp_port')
        SMTP_ACCOUNT  = smtp_config.get('smtp_account')
        SMTP_PASSWORD = smtp_config.get('smtp_password')

# creating Celery instance
backend = os.environ.get("CELERY_RESULT_BACKEND",
                         "db+postgresql://dbc:dbc@localhost:15432/schedule")
broker = os.environ.get("CELERY_BROKER_URL",
                        "redis://:redis123@localhost:16379/0")
celery_app = Celery("tasks", backend=backend, broker=broker)
celery_app.conf.update(
    timezone='America/Los_Angeles',
)
