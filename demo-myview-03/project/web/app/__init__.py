"""project.web.app.__init__"""
from flask import Flask
from flask_appbuilder import AppBuilder, SQLA

from .index import EmailIndexView

# Creating and Configuring Flask App
app = Flask(__name__)
app.config.from_object("project.web.config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, indexview=EmailIndexView)

from . import models, api, views # pylint: disable=C0413
