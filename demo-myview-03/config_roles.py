"""project.web.config_roles"""
import sys
import logging

from project.web.app import appbuilder

logger = logging.getLogger(__name__)

################## get role Admin ############################
role_admin = appbuilder.sm.find_role(appbuilder.sm.auth_role_admin)
if role_admin is None:
    logger.error('Error: the role "Admin" is not found!')
    sys.exit(1)

################# configuring role public ####################
role_public = appbuilder.sm.find_role('Public')
if role_public is None:
    logger.error('Error: the role "Public" is not found!')
    sys.exit(1)

for pv in role_admin.permissions:
    if 'can get on EmailModelApi' == pv.__repr__() or \
       'can post on EmailModelApi' == pv.__repr__() or \
       'can delete on EmailModelApi' == pv.__repr__():
        appbuilder.sm.add_permission_role(role_public, pv)

################ configuring role scheduler ##################
role_scheduler = appbuilder.sm.find_role('scheduler')
if role_scheduler is None:
    appbuilder.sm.add_role('scheduler')
    role_scheduler = appbuilder.sm.find_role('scheduler')

for pv in role_admin.permissions:
    if 'can get on EmailModelApi' == pv.__repr__():
        appbuilder.sm.add_permission_role(role_scheduler, pv)

############### adding admin user ############################
user_admin = appbuilder.sm.add_user(
    username = 'admin', first_name='admin', last_name='fab',
    email='admin@fab1.com', role=role_admin,
    password='admin'
)
