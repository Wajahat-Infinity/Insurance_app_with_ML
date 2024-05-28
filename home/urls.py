from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('prediction', views.prediction, name='prediction'),
    path('contact', views.contact, name='contact')

  
]
