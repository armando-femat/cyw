from django import forms
from compare.models import Ville
from django.forms import ModelForm


class RechercheVille(forms.Form):
    ville = forms.ModelChoiceField(queryset=Ville.objects.all())
    ville.widget.attrs.update({'class': 'form-control'})
    ville.widget.attrs.update(placeholder="Quelle est ta ville ?")

class FormCompare(forms.Form):
    test = forms.BooleanField()

class FormContact(forms.Form):
    email = forms.EmailField()
    ville = forms.Textarea()

    email.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update(placeholder="Ton addresse email !")
