from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboardView, name='dashboardView'),
    path('result', views.resultView, name='resultView'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('check/<int:id>', views.checkView, name='checkView'),
]
