from django.contrib import admin
from .models import Liste, Ville, Critere, Promesse, Categorie, Contact, Candidat


class ListeAdmin(admin.ModelAdmin):
    model=Liste
    list_display = ['nom', 'ville']

admin.site.register(Liste, ListeAdmin)

class VilleAdmin(admin.ModelAdmin):
    model=Ville
    list_display = ['nom']
    search_fields  = ['nom']
admin.site.register(Ville, VilleAdmin)
admin.site.register(Critere)
admin.site.register(Promesse)
admin.site.register(Categorie)
admin.site.register(Contact)
admin.site.register(Candidat)
# Register your models here.
