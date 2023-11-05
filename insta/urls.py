from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('services', services, name='services'),
    path('pricing', pricing, name='pricing'),
    path('car', car, name='car'),
    path('blog', blog, name='blog'),
    path('contact', contact, name='contact'),
    path('blog/<slug:slug>/', blog_single, name='blog_single'),
    path('cars/<slug:slug>/', car_single, name='car_single'),

    path('login/', login_user, name='login_user'),
    path('registration/', registration_user, name='registration_user'),
    path('logout/', logout_user, name='logout_user'),
]
