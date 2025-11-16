app_name = 'todos'

from django.urls import path
from .views import home,create_task,tasks

urlpatterns = [
    path('',home,name='home' ),
    path('create/',create_task,name='create' ),
    path('tasks/',tasks,name='tasks')
]
