from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('board', views.board),
    path('post_message', views.post_message),
    path('delete_message', views.delete_message),
    path('post_comment', views.post_comment),
    path('logout', views.logout),


]
