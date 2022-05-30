from django.urls import path

from . import views


urlpatterns = [

    path("login",views.login_page , name = "login"),
    path("logout",views.logout_page , name = "logout"),
    path("register", views.register_page , name = "register"),

    path("" , views.todo , name = "todo"),
    path("task", views.taskList , name = "task_list"),
    path("task/<int:pk>" , views.detail_view , name = "detail"),
    path("create_task" , views.create_task , name="create_task"),
    path("update-task/<int:pk>" , views.update_task , name = "update_task"),
    path("delete_task/<int:pk>" , views.delete_task , name = 'delete_task'),

]

