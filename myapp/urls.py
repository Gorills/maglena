
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from . sitemaps import *
from turn.views import work, work_detail

sitemaps = {
    'static': StaticViewSitemap,
    'turn': TurnSitemap,
    'service': ServiceSitemap,
    
}


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('work/', work, name='work'),
    path('work/<slug:slug>/', work_detail, name='work_detail'),
    path('about/3d-tour/', views.tour, name='tour'),
    path('vacancy/', views.vacancy, name='vacancy'),
    path('contacts/', views.contacts, name='contacts'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path("robots.txt", views.robots_txt),
    
]