from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='htmx-form-index'),
    path('book-list/', views.book_list, name='book-list')
]