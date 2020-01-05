from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    titre = models.CharField(max_length=100)

    def __str__(self):
        return self.titre


class Critere(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(null=True)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.PROTECT)
    estStandard = models.BooleanField(default=True)

    def __str__(self):
        return self.titre


class Ville(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    criteres = models.ManyToManyField(Critere, related_name='Ville')
    description = models.TextField(null=True)
    population = models.IntegerField(null=True)
    departement = models.CharField(max_length=100, null=True)
    prenomMaire = models.CharField(max_length=100, null=True)
    nomMaire = models.CharField(max_length=100, null=True)
    dateNaissanceMaire = models.DateField(null=True)
    ageMaire = models.IntegerField(null=True)
    sexMaire = models.CharField(max_length=1, null=True)
    ProfessionMaire = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nom

    # def __init__(self, *args, **kwargs):
    #     self.criteres.add(Critere.objects.filter(estStandard=True))


class Liste(models.Model):
    nom = models.CharField(max_length=100)
    slogan = models.CharField(max_length=250, null=True)
    auteur = models.ManyToManyField(User)
    presentation = models.TextField(null=True)
    ville = models.ForeignKey(Ville, on_delete=models.PROTECT, null=True)
    couleur = models.CharField(max_length=100, null=True)
    photo = models.ImageField(null=True)

    class Meta:
        verbose_name = "liste"
        ordering = ['nom']

    def __str__(self):
        return self.nom


class Promesse(models.Model):
    critere = models.ForeignKey(Critere, on_delete=models.PROTECT)
    titre = models.TextField()
    description = models.TextField(null=True)
    liste = models.ForeignKey(Liste, on_delete=models.PROTECT, null=True)
    estUnePriorite = models.BooleanField(default=False)

    def __str__(self):
        return self.liste + ' - ' + self.titre

# class Priorite(models.Model):
#     liste = models.ForeignKey(Liste, on_delete=models.PROTECT)
#     Promesse = models.ForeignKey(Promesse, on_delete=models.PROTECT)
#     Index = models.IntegerField(null=True)


class Contact(models.Model):
    email = models.EmailField(null=True)
    #ville = models.ForeignKey(Ville, on_delete=models.PROTECT, null=True, blank=True)
    ville = models.CharField(max_length=200 ,null=True, blank=True)
    comment = models.TextField(null=True)

    def __str__(self):
        return self.email

class Candidat(models.Model):
    Nom = models.CharField(max_length=100)
    Prenom = models.CharField(max_length=100)
    Liste = models.ForeignKey(Liste, on_delete=models.PROTECT)
    EstTeteDeListe = models.BooleanField(default=False)

    def __str__(self):
        return self.Prenom + ' ' + self.Nom
