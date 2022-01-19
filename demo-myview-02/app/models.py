"""models.py"""
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin


class Projects(Model):
    """Projects Table"""
    id           = Column(Integer, primary_key=True)
    project_name = Column(String(50), unique = True, nullable=False)
    description  = Column(String(300), nullable=True)

    def __repr__(self):
        return self.project_name.__str__()


class Tasks(Model):
    """Tasks Table"""
    id          = Column(Integer, primary_key=True)
    task_name   = Column(String(50), unique=True, nullable=False)
    description = Column(String(300), nullable=True)
    project_id  = Column(Integer, ForeignKey(Projects.id))
    project_tbl = relationship('Projects', foreign_keys='Tasks.project_id')

    def __repr__(self):
        return self.task_name.__str__()


class TaskProgress(AuditMixin, Model):
    """TaskProgress Table"""
    id          = Column(Integer, primary_key=True)
    task_id     = Column(Integer, ForeignKey(Tasks.id))
    start_time  = Column(DateTime, nullable=False)
    end_time    = Column(DateTime, nullable=True)
    status      = Column(Enum('QUEUED', 'STARTED', 'FINISHED', 'FAILED',
                              'PAUSED', 'CANCELED', name='StatusEnum'),
                         default='STARTED', nullable=False)
    comment     = Column(String(300), nullable=True)
    task_tbl    = relationship('Tasks', foreign_keys='TaskProgress.task_id')
