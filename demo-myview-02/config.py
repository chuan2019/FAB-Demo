"""config.py"""
# pylint: disable=R0401
import os
from flask_appbuilder.security.manager import AUTH_DB

basedir = os.path.abspath(os.path.dirname(__file__))

# Your App secret key
SECRET_KEY = r"\2\1thisismyscretkey\1\2\e\y\y\h"

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = 'postgresql://dbc:dbc@localhost:5433/fab_demo_02'

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

# ------------------------------
# GLOBALS FOR APP Builder
# ------------------------------
APP_NAME = "FAB Demo 02"
APP_ICON = "/static/img/demo-logo.png"

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# The authentication type
AUTH_TYPE = AUTH_DB # for database (username/password)

# Setup Full admin role name
AUTH_ROLE_ADMIN = 'Admin'

# Setup Public role name, no authentication needed
AUTH_ROLE_PUBLIC = 'Public'

# User self registration is not allowed
AUTH_USER_REGISTRATION = False

# ---------------------------------------------------
# Image and file configuration
# ---------------------------------------------------
# The file upload folder, when using models with files
UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload folder, when using models with images
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"

# The image upload url, when using models with images
IMG_UPLOAD_URL = "/static/uploads/"
# Setup image size default is (300, 200, True)
IMG_SIZE = (300, 200, True)

# Theme configuration
APP_THEME = "readable.css"
