from django import forms
from compare.models import Ville
from django.forms import ModelForm


class RechercheVille(forms.Form):
    ville = forms.CharField()


class FormCompare(forms.Form):
    test = forms.BooleanField()

