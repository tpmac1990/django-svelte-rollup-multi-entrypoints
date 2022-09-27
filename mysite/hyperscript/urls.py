from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="hyperscript/index.html"), name='hyperscript'),
    path("htmx-get/", views.htmx_get, name='htmx-get'),
]