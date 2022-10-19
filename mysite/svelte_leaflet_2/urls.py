from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="svelte_leaflet_2/index.html"), name='leaflet-index-2'),
]