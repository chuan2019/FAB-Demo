"""project.web.app.api"""
from flask_appbuilder import ModelRestApi
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.models.filters import BaseFilter

from . import appbuilder
from .models import EmailModel

class EmailFilter(BaseFilter): # pylint: disable=R0903
    """user-defined filter for querying email_address by value"""
    name = "Email Address Filter"
    arg_name = "opr"

    def apply(self, query, value):
        print('\n\nEmailFilter is applied!\n\n')
        return query.filter(
            EmailModel.email_address.like(value + "%")
        )


class EmailModelApi(ModelRestApi):
    """RESTful API for exposing email_model table"""
    resource_name = 'recipients'
    datamodel = SQLAInterface(EmailModel)
    allow_browser_login = True

    search_filters = {"email_address": [EmailFilter]}
    openapi_spec_methods = {
        "get_list": {
            "get": {
                "description": "Get all email addresses, filter and pagination",
            }
        }
    }


appbuilder.add_api(EmailModelApi)
