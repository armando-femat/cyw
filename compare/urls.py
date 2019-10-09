from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('liste/<int:id>', views.liste, name='Liste'),
    path('accueil', views.accueil, name='accueil'),
    path('compare/<str:nom>', views.compare, name='compare'),
    path('<str:nom>', views.ville, name='ville'),
]
