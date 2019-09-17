from django import forms
from compare.models import Ville


class RechercheVille(forms.Form):
    ville = forms.CharField()

