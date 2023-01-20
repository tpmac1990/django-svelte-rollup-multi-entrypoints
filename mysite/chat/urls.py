from django.urls import path 
from chat import views 

urlpatterns = [
    path('', views.lobby, name='chat')
]