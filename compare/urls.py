from django.contrib import admin
from django.urls import path, re_path
from . import views
from dal import autocomplete
from . import models
from .viewObject import VilleAutocomplete


urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('liste/<int:id>', views.liste, name='Liste'),
    path('test', views.test, name='test'),
    path('compare/<str:nom>', views.compare, name='compare'),
    re_path('ville-autocomplete/$', VilleAutocomplete.as_view(model=models.Ville), name='ville-autocomplete'),
    path('<str:nom>', views.ville, name='ville'),	
]
