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
        queryset=Liste.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
         )

class FormContact(forms.Form):
    email = forms.EmailField()
    email.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update(placeholder="Mon adresse mail")
    villeContact = forms.CharField(max_length=200)
    villeContact.widget.attrs.update({'class': 'form-control'})
    villeContact.widget.attrs.update(placeholder="Quelle est ta ville ?")
    comment = forms.CharField(widget=forms.Textarea)
    comment.widget.attrs.update({'class': 'form-control'})
    comment.widget.attrs.update(placeholder="Nous sommes à l'écoute !")
    comment.widget.attrs.update(rows ="4")

class FormInfo(forms.Form):
    email = forms.EmailField()
    email.widget.attrs.update(placeholder="Ton adresse email !")
    email.widget.attrs.update({'class': 'form-control-black form-group'})





