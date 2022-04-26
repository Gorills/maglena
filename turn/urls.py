

from django.urls import path
from . import views

urlpatterns = [
    path('', views.turn, name='turn'),
    path('<slug:slug>/', views.turn_detail, name='turn_detail'),
   
    path('<slug:parent>/<slug:slug>/', views.servise_list, name='servise_list'),


]
