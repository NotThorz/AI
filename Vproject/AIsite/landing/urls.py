from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('logout', auth_views.LogoutView.as_view(
        next_page='home'), name='logout'),
    path('blog', views.blog, name='blog'),
    path('content', views.content, name='content'),
    path('login', views.login, name='login'),
    path('emails', views.emails, name='emails')
]
