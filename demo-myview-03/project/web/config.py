"""project.web.config"""
import os
from flask_appbuilder.security.manager import AUTH_DB

basedir = os.path.abspath(os.path.dirname(__file__))

# Your App secret key
SECRET_KEY = r"\2\1thisismyscretkey\1\2\e\y\y\h"

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")

SQLALCHEMY_BINDS = {
    'web_db': 'sqlite:///' + os.path.join(basedir, 'web.db')
}

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

# ------------------------------
# GLOBALS FOR APP Builder
# ------------------------------
FAB_API_SWAGGER_UI = True

APP_NAME = "Demo-04"
APP_ICON = "/static/img/demo-logo.png"

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# The authentication type
AUTH_TYPE = AUTH_DB

# Full admin role name
AUTH_ROLE_ADMIN = 'Admin'

# Setup Public role name, no authentication needed
AUTH_ROLE_PUBLIC = 'Public'

# Will not allow user self registration
AUTH_USER_REGISTRATION = False

# Theme configuration
APP_THEME = "../../../css/my_readable.css"
