from django.core.checks.messages import Info
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
  path('', views.redir),
  path('shows', views.index),
  path('shows/new', views.newshow),
  path('shows/create', views.create),
  path('shows/<showid>', views.info),
  path('shows/<showid>/edit', views.edit),
  path('shows/<showid>/update', views.update),
  path('shows/<showid>/destroy', views.delete),
]