from django.urls import path
from .views import create_task, assign_task, get_user_tasks

urlpatterns = [
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/<int:task_id>/assign/', assign_task, name='assign_task'),
    path('tasks/user/<int:user_id>/', get_user_tasks, name='get_user_tasks'),
]
