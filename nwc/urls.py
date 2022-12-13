from django.urls import path
from . import views
from django.contrib import admin

# app_name = "nwc"


urlpatterns = [
    path("login/", views.LogInView.as_view(), name="Login",),
    path("logout/", views.LogoutView.as_view(), name="Logout",),
    path("protected/", views.ProtectedView.as_view(), name="protected",),
    # path('', views.home, name="home"),
    # path('register', views.register, name="register"),
    # path('signin', views.signin, name="signin"),
    # path('signout', views.signout, name="signout"),
]
