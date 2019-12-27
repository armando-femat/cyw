from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from compare.models import Liste, Promesse, Ville, Categorie, Contact
from compare.form import RechercheVille, FormCompare, FormContact
from compare.viewObject import vCategorie
from dal import autocomplete


def liste(request, id):
    l = get_object_or_404(Liste, id=id)
    ps = Promesse.objects.filter(liste_id=id)
    cats = Categorie.objects.all()
    prio = Promesse.objects.filter(liste_id=id, estUnePriorite=True)
    return render(request, 'compare/liste.html', locals())


def ville(request, nom):
    form = FormCompare(request.POST or None)
    if form.is_valid():
        a = form.cleaned_data['test']
        if a:
            print("ok")
        else:
            print("nok")
    v = get_object_or_404(Ville, nom=nom)
    #form.fields['Listes'].queryset = [l.pk for l in Liste.objects.filter(ville=v)]
    ls = Liste.objects.filter(ville=v)
    return render(request, 'compare/ville.html', locals())


def accueil(request):
    formV = RechercheVille(request.POST or None)
    formC = FormContact(request.POST or None)
    modal = False
    print("ok1")
    if formV.is_valid():
        print("ok")
        nom = formV.cleaned_data['ville']
        print(nom.id)
        return redirect(ville, nom)
    if formC.is_valid():
        email = formC.cleaned_data['email']
        c = Contact(email=email)
        c.save()
        modal = True
    return render(request, 'compare/accueil.html', locals())


def test(request):
    form = RechercheVille(request.POST or None)
    if form.is_valid():
        print("ok")
        nom = form.cleaned_data['ville']
        return redirect(ville, id=nom)
    return render(request, 'compare/test.html', locals())


def compare(request, nom):
    vcats = []
    cs = Categorie.objects.all()
    v = get_object_or_404(Ville, nom=nom)
    ls = Liste.objects.filter(ville=v)
    for cat in cs:
        vcats.append(vCategorie(cat, v, ls))
    return render(request, 'compare/compare.html', locals())


