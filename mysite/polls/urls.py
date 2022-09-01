from django.urls import path

from .views import PollQuestions, Others, index


urlpatterns = [
    path('', index, name='index'),
    path('questions/', PollQuestions.as_view(), name='questions'),
    path('other/', Others.as_view(), name='others')
]