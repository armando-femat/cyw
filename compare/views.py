from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from compare.models import Liste, Promesse, Ville, Categorie, Contact, Critere
from compare.form import RechercheVille, FormCompare, FormContact, FormInfo
from compare.viewObject import vCategorie
from datetime import datetime
from django.contrib.staticfiles.templatetags.staticfiles import static
import csv


def liste(request, id):
    l = get_object_or_404(Liste, id=id)
    ps = Promesse.objects.filter(liste_id=id)
    cats = Categorie.objects.all()
    prio = Promesse.objects.filter(liste_id=id, estUnePriorite=True)
    return render(request, 'compare/liste.html', locals())


def ville(request, url):
    form = FormCompare(request.POST or None)
    formC = FormInfo(request.POST or None)
    v = get_object_or_404(Ville, url=url)
    print(v)
    #form.fields['Listes'].queryset = [l.pk for l in Liste.objects.filter(ville=v)]
    ls = Liste.objects.filter(ville=v).order_by('?')
    for l in ls:
        l.prio = Promesse.objects.filter(liste=l, estUnePriorite=True)
    if formC.is_valid():
        email = formC.cleaned_data['email']
        villeContact = get_object_or_404(Ville, url=url)
        c = Contact(email=email, ville=villeContact, comment = "Je veux rester informé")
        c.save()
        return redirect('/#aide')
    if form.is_valid():
        listes=request.POST.getlist('Listes',default=None)
        return compare(request, url, listes=listes)
    return render(request, 'compare/ville.html', locals())


def compare(request, url, **kwargs):
    vcats = []
    cs = Categorie.objects.all()
    v = get_object_or_404(Ville, url=url)
    ids = kwargs.get('listes', None)
    ls=[]
    if len(ids)>0 :
        ls = Liste.objects.filter(id__in = ids)
    else:
        ls = Liste.objects.filter(ville=v)
    for l in ls:
        l.prio=[]
        l.prio.extend(Promesse.objects.filter(liste=l, estUnePriorite=True))
    for cat in cs:
        vcats.append(vCategorie(cat, v, ls))
    return render(request, 'compare/compare.html', locals())


def accueil(request, **kwargs):
    formV = RechercheVille(request.POST or None)
    formC = FormContact(request.POST or None)
    cs = Categorie.objects.all()
    verif = (datetime.strptime("07/02/2020", "%d/%m/%Y") - datetime.now()).days
    premier = (datetime.strptime("15/03/2020", "%d/%m/%Y") - datetime.now()).days
    for c in cs:
        c.criteres = []
        c.criteres.extend(Critere.objects.filter(categorie=c, estStandard=True))
    modal = kwargs.get('modal', False)
    if formV.is_valid():
        nom = formV.cleaned_data['ville']
        v = get_object_or_404(Ville, nom=nom)
        return redirect(ville, v.url)
    if formC.is_valid():
        email = formC.cleaned_data['email']
        villeContact = formC.cleaned_data['villeContact']
        comment = formC.cleaned_data['comment']
        c = Contact(email=email, ville=villeContact, comment=comment)
        c.save()
        modal = True
    return render(request, 'compare/accueil.html', locals())


def test(request):
    vs = Ville.objects.all()
    for v in vs:
        v.url = v.nom.replace(" ","").replace("é","e").replace("ô","o").replace("è","e").replace("î","i")
        v.save()
    return render(request, 'compare/testold.html', locals())


