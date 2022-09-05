from django.urls import path
from .views import Others


urlpatterns = [
    path('', Others.as_view(), name='others')
]