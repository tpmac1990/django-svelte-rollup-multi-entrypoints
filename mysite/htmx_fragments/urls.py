from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="htmx_fragments/index.html"), name='htmx-fragments-index'),
    path('get-item-list/', views.item_list , name='item-list'),
    path('delete-item/<int:id>/', views.delete_item , name='delete-item'),

    path('form-fragment/', views.form_page, name='form-fragment'),
    path('basic-form/', views.basic_form, name='basic-form'),

    path('get-img-app/', views.img_app, name='img-app'),
    path('get-img-app-prev/<int:pk>/', views.img_app_prev, name='img-app-prev'),
    path('get-img-app-next/<int:pk>/', views.img_app_next, name='img-app-next'),

]