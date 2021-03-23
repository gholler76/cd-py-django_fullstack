from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.shows_new),
    path('shows/create', views.shows_create),
    path('shows/<int:num>', views.shows_info),
    path('shows/<int:num>/edit', views.shows_edit),
    path("shows/<int:num>/update", views.shows_update),
    path("shows/<int:num>/destroy", views.shows_destroy)


]
