from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('register_app.routes')),

]
