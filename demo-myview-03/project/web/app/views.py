"""project.web.app.views"""
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView

from . import appbuilder, db
from .models import EmailModel

class EmailModelView(ModelView):
    """ModelView for the EmailModel"""
    datamodel = SQLAInterface(EmailModel)
    list_columns = ['id', 'email_address']

db.create_all()

appbuilder.add_view(
    EmailModelView,
    "List Emails",
    icon = "fa-folder-open-o",
    category = "Emails",
    category_icon = "fa-envelope"
)

# Application wide 404 error handler
@appbuilder.app.errorhandler(404)
def page_not_found(e): # pylint: disable=C0103,W0613
    """page when 404 error occurs"""
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )
