from django.urls import path
from . import views_manager, views_user

urlpatterns = [
    # Manager
    path("projects/", views_manager.project_list, name="project_list"),
    path("projects/add/", views_manager.project_create, name="project_create"),
    path("projects/edit/<int:pk>/", views_manager.project_edit, name="project_edit"),
    path("projects/delete/<int:pk>/", views_manager.project_delete, name="project_delete"),

    path("tasks/", views_manager.task_list, name="task_list"),
    path("tasks/add/", views_manager.task_create, name="task_create"),
    path("tasks/edit/<int:pk>/", views_manager.task_edit, name="task_edit"),
    path("tasks/delete/<int:pk>/", views_manager.task_delete, name="task_delete"),

    # User
    path("my-tasks/", views_user.my_tasks, name="my_tasks"),
    
]
