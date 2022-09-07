from django.urls import path
from .views import Sform, todo

urlpatterns = [
    path('', Sform.as_view(), name='sform'),
    path('todo', todo, name='todo')
]