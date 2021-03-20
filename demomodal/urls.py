from django.urls import path
from .views import HomeView
from . import views

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handleLogIn, name="handleLogin"),
    path('logout', views.handleLogOut, name="handleLogout"),
]
