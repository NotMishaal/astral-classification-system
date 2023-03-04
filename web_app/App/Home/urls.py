from django.urls import path 
from . import views
 
urlpatterns = [
    path('',views.homeView,name='homeView'), 
    path('about', views.aboutView, name='aboutView'),
    path('team', views.teamView, name='teamView'),
]
