from django import forms
from compare.models import Ville
from django.forms import ModelForm


class RechercheVille(forms.Form):
    ville = forms.ModelChoiceField(queryset=Ville.objects.all(),
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control','placeholder':"Quelle est ta ville ?"}))

class FormCompare(forms.Form):
    test = forms.BooleanField()


class FormContact(forms.Form):
    email = forms.EmailField()
    ville = forms.Textarea()