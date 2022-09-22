from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="alpine/index.html"), name='alpine'),
    path("get-partial/", TemplateView.as_view(template_name="alpine/partial.html"), name='get-partial'),
]