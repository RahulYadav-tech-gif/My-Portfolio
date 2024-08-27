from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('projects/', views.projects, name="projects"),
    path('experiences/', views.experiences, name="experiences"),
    path('certifications/', views.certifications, name="certifications"),
    path('contact/', views.contact, name="contact"),
    path('resume/', views.resume, name="resume"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)