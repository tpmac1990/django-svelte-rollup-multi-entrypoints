from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="alpine/index.html"), name='alpine'),
    path("get-partial/", TemplateView.as_view(template_name="alpine/partial.html"), name='get-partial'),
]