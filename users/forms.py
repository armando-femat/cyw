from django import forms
from django.forms import ModelForm
from compare.models import Ville, Liste
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from dal import autocomplete


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ListForm(ModelForm):
    ville = forms.ModelChoiceField(queryset=Ville.objects.all(),
                                   widget=autocomplete.ModelSelect2(url='ville-autocomplete'))
    class Meta:
        model = Liste
        fields = ['ville', 'nom', 'couleur', 'teteDeListe', 'presentation', 'site']
