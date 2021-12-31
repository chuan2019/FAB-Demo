from flask import render_template, g
from flask_login import AnonymousUserMixin
from sqlalchemy import or_
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.filters import FilterEqualFunction
from flask_appbuilder.models.filters import BaseFilter
from . import appbuilder, db
from .models import Projects, Tasks, TaskProgress


class CustomAdminFilter(BaseFilter):
    def apply(self, query, value):
        role_admin = appbuilder.sm.find_role(appbuilder.sm.auth_role_admin)
        if g.user.is_anonymous:
            return query
        if not role_admin in g.user.roles:
            return query.filter(or_(TaskProgress.created_by == g.user, TaskProgress.changed_by == g.user))
        else:
            return query

class TaskProgressModelView(ModelView):
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

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

