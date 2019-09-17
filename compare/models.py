from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Critere(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField(null=True)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.titre

class Ville(models.Model):
    nom = models.CharField(max_length=100)
    criteres = models.ManyToManyField(Critere, related_name='Ville')

    def __str__(self):
        return self.nom

class Liste(models.Model):
    nom = models.CharField(max_length=100)
    auteur = models.ManyToManyField(User)
    presentation = models.TextField(null=True)
    ville = models.ForeignKey(Ville, on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = "liste"
        ordering = ['nom']

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        return self.nom


class Promesse(models.Model):
    critere = models.ForeignKey(Critere, on_delete=models.PROTECT)
    titre = models.TextField()
    description = models.TextField(null=True)
    liste = models.ForeignKey(Liste, on_delete=models.PROTECT, null=True)
    estUnEngagement = models.BooleanField(default=False)

    def __str__(self):
        return self.titre