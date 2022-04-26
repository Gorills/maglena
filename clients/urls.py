from django.urls import path
from . import views




urlpatterns = [
    path('', views.rewiew, name='rewiew'),
    path('create/', views.rewiew_create, name='rewiew_create'),
    path('add/', views.ContactView.as_view(), name='contact')

   
]