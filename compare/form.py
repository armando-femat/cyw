from django import forms
from compare.models import Ville, Liste
from dal import autocomplete
from django.shortcuts import get_object_or_404


class RechercheVille(forms.Form):
    ville = forms.ModelChoiceField(queryset=Ville.objects.all(), widget=autocomplete.ModelSelect2(url='ville-autocomplete'))
    ville.widget.attrs.update({'class': 'form-home'})
    #ville.widget.attrs.update(placeholder="Quelle est ta ville ?")


class FormCompare(forms.Form):
    Listes = forms.ModelMultipleChoiceField(
<<<<<<< HEAD
        queryset=Liste.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
=======
         queryset=Liste.objects.all(),
         widget=forms.CheckboxSelectMultiple,
>>>>>>> 328280343895a2eafe40b852c63b1f3aaf732900
         )

class FormContact(forms.Form):
    email = forms.EmailField()
    ville = forms.Textarea()
    email.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update(placeholder="Ton addresse email !")


