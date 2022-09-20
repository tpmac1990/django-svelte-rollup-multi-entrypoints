from django.urls import path
from . import views

urlpatterns = [
    path("films/", views.FilmList.as_view(), name='film-list'),
    path("films/<slug:slug>/", views.FilmDetail.as_view(), name='film'),
]

htmx_urlpatterns = [
    path('add-film/', views.add_film, name='add-film'),
    path('delete-film/<int:pk>/', views.delete_film, name='delete-film'),
    path('search-film/', views.search_film, name='search-film'),
    path('clear/', views.clear, name='clear'),
    path('sort/', views.sort, name='sort'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('film-list-partial', views.films_partial, name='film-list-partial'),
    path('upload-photo/<int:pk>/', views.upload_photo, name='upload-photo'),
    path('film-count/', views.film_count, name='film-count'),
]

urlpatterns += htmx_urlpatterns