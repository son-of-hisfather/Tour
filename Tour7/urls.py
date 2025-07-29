from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('destinations/', views.destinations, name='destinations'),
    path('destination/', views.destination_details, name='destination_details'),
    path('contact/', views.contact, name='contact'),
    path('tours/', views.tours, name='tours'),
    path('gallery/', views.gallery, name='gallery'),
]
    
