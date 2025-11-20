from django.urls import path
from . import views

urlpatterns = [
     path('', views.dashboard_home, name='dashboard_home'),
    path("users/", views.user_list, name="user_list"),
    path("users/add/", views.user_create, name="user_create"),
    path("users/edit/<int:pk>/", views.user_edit, name="user_edit"),
    path("users/delete/<int:pk>/", views.user_delete, name="user_delete"),
    path("users/export/csv/", views.export_users_csv, name="export_users_csv"),
]
