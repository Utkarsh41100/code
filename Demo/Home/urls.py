from django.contrib import admin
from django.urls import path, include 
from Home import views
urlpatterns = [
    path("", views.index, name='Home'),  ## redirect index function of views file
    path("about", views.about, name='about'),
    path("profile", views.profile, name='profile'),   
]
