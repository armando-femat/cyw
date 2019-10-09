from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from compare.models import Liste, Promesse, Ville, Categorie
from compare.form import RechercheVille, FormCompare
from compare.viewObject import vCategorie


def liste(request, id):
    l = get_object_or_404(Liste, id=id)
    ps = Promesse.objects.filter(liste_id=id)
    cats = Categorie.objects.all()
    return render(request, 'compare/liste.html', locals())


def ville(request, nom):
    form = FormCompare(request.POST or None)
    print("blabl")
    if form.is_valid():
        print("ok")
    v = get_object_or_404(Ville, nom=nom)
    ls = Liste.objects.filter(ville=v)
    return render(request, 'compare/ville.html', locals())


def accueil(request):
    form = RechercheVille(request.POST or None)
    if form.is_valid():
        nom = form.cleaned_data['ville']
        return redirect(ville, nom=nom)
    return render(request, 'compare/accueil.html', locals())


def compare(request, nom):
    vcats = []
    cs = Categorie.objects.all()
    v = get_object_or_404(Ville, nom=nom)
    ls = Liste.objects.filter(ville=v)
    for cat in cs:
        vcats.append(vCategorie(cat, v, ls))
    return render(request, 'compare/compare.html', locals())
