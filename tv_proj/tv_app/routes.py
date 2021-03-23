from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/<num>', views.shows_info),
    path('shows/<num>/edit', views.shows_edit),
    path("shows/<num>/update", views.shows_update),
    path('shows/new', views.shows_new),
    path('shows/create', views.shows_create),
    path("shows/<num>/destroy", views.shows_destroy),


]
