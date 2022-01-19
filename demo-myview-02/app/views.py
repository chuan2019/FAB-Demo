"""views.py"""
from flask import g
from sqlalchemy import or_
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from flask_appbuilder.models.filters import BaseFilter
from app import appbuilder, db
from app.models import Projects, Tasks, TaskProgress


# pylint: disable=R0903
class CustomAdminFilter(BaseFilter):
    """
    User defined filter
    Purpose: if user is not registered (in public domain), all records are returned
             if user is registered but not admin, only records created or changed by
             them are returned
             if user has admin permission, all records are returned
    """
    def apply(self, query, value):
        role_admin = appbuilder.sm.find_role(appbuilder.sm.auth_role_admin)
        if g.user.is_anonymous:
            return query
        if not role_admin in g.user.roles:
            return query.filter(or_(TaskProgress.created_by == g.user,
                                    TaskProgress.changed_by == g.user))
        return query

class TaskProgressModelView(ModelView):
    """Model View for the TaskProgress Table"""
    datamodel = SQLAInterface(TaskProgress)

    label_columns = {'task_progress':'Task Progress'}
    list_columns = ['task_id','start_time','end_time','created_by','created_on',
                    'changed_by','changed_on','status','comment']
    edit_exclude_columns = ['created_by', 'created_on', 'changed_by', 'changed_on']
    add_exclude_columns = ['created_by', 'created_on', 'changed_by', 'changed_on']
    show_fieldsets = [
        (
            'Task Progress',
            {'fields': ['task_id','start_time','end_time','created_by','created_on',
                        'changed_by','changed_on','status','comment']}
        ),
    ]
    base_filters = [['', CustomAdminFilter, None]]

class ProjectModelView(ModelView):
    """Model View for the Projects Table"""
    datamodel = SQLAInterface(Projects)
    related_views = [TaskProgressModelView]

    label_columns = {'projects':'Projects'}
    list_columns = ['id','project_name','description']
    show_fieldsets = [
        (
            'Projects',
            {'fields': ['id', 'project_name', 'description']}
        ),
    ]

class TaskModelView(ModelView):
    """Model View for the Tasks Table"""
    datamodel = SQLAInterface(Tasks)
    related_views = [TaskProgressModelView]

    label_columns = {'tasks':'Tasks'}
    list_columns = ['id','task_name','description','project_id']
    show_fieldsets = [
        (
            'Tasks',
            {'fields': ['id', 'task_name', 'description', 'project_id']}
        ),
    ]


db.create_all()
appbuilder.add_view(
    ProjectModelView,
    "List Projects",
    icon = "fa-folder-open-o",
    category = "Projects",
    category_icon = "fa-envelope"
)
appbuilder.add_view(
    TaskModelView,
    "List Tasks",
    icon = "fa-folder-open-o",
    category = "Tasks",
    category_icon = "fa-envelope"
)
appbuilder.add_view(
    TaskProgressModelView,
    "List Task Progress",
    icon = "fa-folder-open-o",
    category = "Tasks Projects",
    category_icon = "fa-envelope"
)
