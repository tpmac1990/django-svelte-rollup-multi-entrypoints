from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    # path('', TemplateView.as_view(template_name="svelte_demo/index.html"), name='svelte-demo-index'),
    path('', views.SvelteDemos.as_view(), name='svelte-demo-index'),

    path('clubs/', views.clubs, name='svelte-demo-clubs'),
    path('hobbies/', views.hobbies, name='svelte-demo-hobbies')
]