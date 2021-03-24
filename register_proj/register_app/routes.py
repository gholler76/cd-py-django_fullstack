from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('hello', views.hello),
    path('hello/create', views.register),
    path('hello/success', views.success),
    path('hello/login', views.login),
    path('hello/logout', views.logout),


]
