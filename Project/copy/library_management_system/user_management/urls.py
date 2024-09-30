from django.contrib import admin
from django.urls import path , include
from user_management import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.guest, name='Home'),
    path("about_us", views.about_us, name='about_us'),
    path("contact_us", views.about_us, name='contact_us'),
    path("profile", views.profile, name='profile'),  
    path("login", views.login, name='login'),  
    path("user_login", views.user_login, name='user_login'),  
]