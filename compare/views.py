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
    v = get_object_or_404(Ville, nom=nom)
    #form.fields['Listes'].queryset = [l.pk for l in Liste.objects.filter(ville=v)]
    ls = Liste.objects.filter(ville=v)
    if form.is_valid():
        print("ok")
        listes=request.POST.getlist('Listes',default=None)
        return compare(request, nom, listes=listes)
    return render(request, 'compare/ville.html', locals())


def compare(request, nom, **kwargs):
    vcats = []
    cs = Categorie.objects.all()
    v = get_object_or_404(Ville, nom=nom)
    ids = kwargs.get('listes', None)
    if len(ids)>0 :
        ls = Liste.objects.filter(id__in = ids)
    else:
        ls = Liste.objects.filter(ville=v)

    for cat in cs:
        vcats.append(vCategorie(cat, v, ls))
    return render(request, 'compare/compare.html', locals())


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
    nom='Villeurbanne'
    form = FormCompare(request.POST or None)
    v = get_object_or_404(Ville, nom=nom)
    ls = Liste.objects.filter(ville=v)
    if form.is_valid():
        print("ok")
        a=request.POST.getlist('Listes',default=None)
        print(a)
        vs=[]
        for b in a:
            vs.append(b)
            print(vs)
        return compare(request, nom, listes=vs)
    return render(request, 'compare/test.html', locals())




