from django.urls import path

from .views import todo_tasks


urlpatterns = [
    path('', todo_tasks, name='todo'),
]