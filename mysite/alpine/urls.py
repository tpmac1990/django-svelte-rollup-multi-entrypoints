from django.urls import path
from django.views.generic import TemplateView
from alpine import views

urlpatterns = [
    path("", views.alpine_index, name='alpine-index'),
    path("get-partial/", TemplateView.as_view(template_name="alpine/partial.html"), name='get-partial'),

    # gets list of films with taggit tags
    path("taggit-films/", views.FilmListAPIView.as_view(), name='taggit-films')
]