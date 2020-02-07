from django.contrib import admin
from .models import Liste, Ville, Critere, Promesse, Categorie, Contact
from django.contrib.auth.models import User


def addAdmin(modeladmin, request, queryset):
    for Liste in queryset:
        Liste.auteur.add(*User.objects.filter(is_superuser=True))
        Liste.save()

addAdmin.short_description = 'Ajouter les admins'

class ListeAdmin(admin.ModelAdmin):
    model = Liste
    list_display = ['__str__', 'nom', 'teteDeListe', 'couleur', 'ville']
    search_fields = ['nom', 'couleur', 'teteDeListe', 'ville__nom']
    list_filter = (('ville', admin.RelatedOnlyFieldListFilter),)
    actions = [addAdmin, ]
    # fields = ('nom', 'teteDeListe', 'ville', 'couleur', 'lienPhoto','photo', 'presentation', 'slogan', 'site', 'auteur') #Réordonner ou Uniquement ces champs affichés dans le formulaire
    empty_value_display = '-------'
    filter_horizontal = ('auteur',)
    list_display_links = ('__str__', 'nom', 'teteDeListe', 'couleur')
    autocomplete_fields = ['ville']
    # list_select_related = ('ville',)
    save_on_top = True
    fieldsets = (
        (None, {
            'fields': (
                ('nom', 'teteDeListe', 'couleur'), 'ville', 'lienPhoto', 'photo', 'presentation', 'slogan', 'site',
                'auteur')
        }),
        # ('Advanced options', {
        #     'classes': ('collapse',),
        #     'fields': ('registration_required', 'template_name'),
        # }),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "ville":
            kwargs["queryset"] = Ville.objects.filter(ouverte=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Liste, ListeAdmin)


def ouvrir(modeladmin, request, queryset):
    for Ville in queryset:
        Ville.ouverte = True
        Ville.save()


ouvrir.short_description = 'Ouvrir'


def fermer(modeladmin, request, queryset):
    for Ville in queryset:
        Ville.ouverte = False
        Ville.save()


fermer.short_description = 'Fermer'


def ajouterCriteres(modeladmin, request, queryset):
    for Ville in queryset:
        Ville.criteres.add(*Critere.objects.filter(estStandard=True))
        Ville.save()

ajouterCriteres.short_description = 'Ajouter les critères standards'




class VilleAdmin(admin.ModelAdmin):
    model = Ville
    list_display = ['nom', 'departement', 'population', 'ouverte']
    ordering = ('-ouverte', '-population',)
    search_fields = ['nom']
    filter_horizontal = ('criteres',)
    actions = [ouvrir, fermer, ajouterCriteres,]


admin.site.register(Ville, VilleAdmin)
admin.site.register(Critere)
admin.site.register(Promesse)
admin.site.register(Categorie)


class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['email', 'date', 'source', 'ville', 'liste']
    ordering = ('-date',)
    radio_fields = {"source": admin.VERTICAL}


admin.site.register(Contact, ContactAdmin)
# Register your models here.
