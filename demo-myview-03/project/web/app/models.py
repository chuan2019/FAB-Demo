"""project.web.app.models"""
from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey

class EmailModel(Model):
    """
    the extremely simple data model, it only has one single
    column, which is also the primary key
    """
    __bind_key__ = 'web_db'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(64), nullable=False, unique=True)

    def __repr__(self) -> str:
        return self.email_address

