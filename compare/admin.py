from django.contrib import admin
from .models import Liste, Ville, Critere, Promesse, Categorie, Contact


class ListeAdmin(admin.ModelAdmin):
    model=Liste
    list_display = ['nom', 'teteDeListe', 'couleur','ville']
    search_fields  = ['nom', 'couleur', 'teteDeListe']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "ville":
            kwargs["queryset"] = Ville.objects.filter(ouverte=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(Liste, ListeAdmin)


def ouvrir(modeladmin, request, queryset):
    for Ville in queryset:
        Ville.ouverte=True
        Ville.save()
ouvrir.short_description = 'Ouvrir'

def fermer(modeladmin, request, queryset):
    for Ville in queryset:
        Ville.ouverte=False
        Ville.save()
fermer.short_description = 'Fermer'

def ajouterCriteres(modeladmin, request, queryset):
    for Ville in queryset:
        Ville.criteres.add(*Critere.objects.filter(estStandard=True))
        Ville.save()
ajouterCriteres.short_description = 'Ajouter les critères standards'

class VilleAdmin(admin.ModelAdmin):
    model=Ville
    list_display = ['nom', 'departement','population','ouverte']
    ordering = ('-ouverte','-population',)
    search_fields  = ['nom']
    actions = [ouvrir, fermer, ajouterCriteres]
admin.site.register(Ville, VilleAdmin)
admin.site.register(Critere)
admin.site.register(Promesse)
admin.site.register(Categorie)
admin.site.register(Contact)
# Register your models here.
