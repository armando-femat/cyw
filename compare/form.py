from django import forms


class RechercheVille(forms.Form):
    ville = forms.CharField(max_length=100)
