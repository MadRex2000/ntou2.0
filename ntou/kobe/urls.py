from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('coc/', views.coc, name = 'coc'),
    path('about/', views.about, name = 'about'),
    path('post/', views.postSystem, name = 'post'),
    path('postlist/', views.postlist, name = 'postlist'),
    path('registration/', views.registration, name = 'registration'),
    path('contribution/', views.contribution, name = 'contribution'),
    path('registrationSuccess/', views.registrationSuccess, name = 'registrationSuccess'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
