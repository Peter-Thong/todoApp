from django.urls import path
from .views import (addTaskView, updateTaskView, deleteTaskView)

app_name='tasks'
urlpatterns = [
    path('', addTaskView, name='task_list'),
    path('<int:id>/update', updateTaskView, name='task_update'),
    path('<int:id>/delete', deleteTaskView, name='task_delete'),
]
