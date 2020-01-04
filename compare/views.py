from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from compare.models import Liste, Promesse, Ville, Categorie, Contact, Critere
from compare.form import RechercheVille, FormCompare, FormContact
from compare.viewObject import vCategorie
from datetime import datetime
import csv


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
    cs = Categorie.objects.all()
    for c in cs:
        c.criteres = []
        c.criteres.extend(Critere.objects.filter(categorie=c, estStandard=True))
        print(c.criteres)
    modal = False
    if formV.is_valid():
        nom = formV.cleaned_data['ville']
        print(nom.id)
        return redirect(ville, nom)
    if formC.is_valid():
        email = formC.cleaned_data['email']
        villeContact = formC.cleaned_data['villeContact']
        comment = formC.cleaned_data['comment']
        c = Contact(email=email, ville=villeContact, comment=comment)
        c.save()
        modal = True
    return render(request, 'compare/accueil.html', locals())


def test(request):
    with open('C:\\Python\\maires-17-06-2014\\maires-17-06-2014.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        i = 0
        for row in reader:
            if i>1:
                v=Ville.objects.filter(nom=row[2])
                if len(v) == 0:
                    v = Ville(nom=row[2], departement=row[1], population=row[3], nomMaire=row[4], prenomMaire=row[5],
                              sexMaire=row[6], dateNaissanceMaire=datetime.strptime(row[7], "%d/%m/%Y"), ProfessionMaire=row[9])
                    v.save()
                elif v[0].population is None or v[0].population<=int(row[3]):
                    v[0].departement=row[1]
                    v[0].population=row[3]
                    v[0].nomMaire=row[4]
                    v[0].prenomMaire=row[5]
                    v[0].sexMaire=row[6]
                    v[0].dateNaissanceMaire=datetime.strptime(row[7], "%d/%m/%Y")
                    v[0].ageMaire=datetime.now().year-datetime.strptime(row[7], "%d/%m/%Y").year
                    v[0].ProfessionMaire=row[9]
                    v[0].save()
            i += 1
    return render(request, 'compare/testold.html', locals())

