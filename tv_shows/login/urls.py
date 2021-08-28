from django.core.checks.messages import Info
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
  path('', views.register),
  path('/login', views.login),
  path('/mainpage', views.mainpage),
  path('/logout', views.logout),
]