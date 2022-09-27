from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="svelte_leaflet/index.html"), name='leaflet-index'),
]