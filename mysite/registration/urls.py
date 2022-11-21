from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path('check_email/', views.check_email, name='check-email'),
]