from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from compare.models import Liste, Promesse, Ville, Categorie, Contact, Critere
from compare.form import RechercheVille, FormCompare, FormContact, FormInfo, FormContactBlack
from compare.viewObject import vCategorie
from datetime import datetime
from django.contrib.staticfiles.templatetags.staticfiles import static


def liste(request, id):
    formR = FormInfo(request.POST or None)
    formS = FormContactBlack(request.POST or None)
    l = get_object_or_404(Liste, id=id)
    ps = Promesse.objects.filter(liste_id=id)
    cats = Categorie.objects.all()
    prio = Promesse.objects.filter(liste_id=id, estUnePriorite=True)
    user = request.user
    modif=False
    if user in l.auteur.all() :
        modif=True
    if formS.is_valid() and 'signaler' in request.POST :
        email = formS.cleaned_data['email']
        comment = formS.cleaned_data['comment']
        inform = formS.cleaned_data['inform']
        c = Contact(email=email, comment=comment, source='SIN', resteInforme=inform, ville=l.ville, liste=l)
        c.save()
        modalSignal = True
    if formR.is_valid() and 'formR' in request.POST :
        email = formR.cleaned_data['email']
        c = Contact(email=email, ville=l.ville, source='LST', liste=l)
        c.save()
        modalFollow = True
    return render(request, 'compare/liste.html', locals())


def ville(request, url, **kwargs):
    formC = FormCompare(request.POST or None)
    formI = FormInfo(request.POST or None)
    formR = FormInfo(request.POST or None)
    formS = FormContactBlack(request.POST or None)
    v = get_object_or_404(Ville, url=url)
    #form.fields['Listes'].queryset = [l.pk for l in Liste.objects.filter(ville=v)]
    ls = Liste.objects.filter(ville=v).order_by('?')
    iframe = kwargs.get('iframe', True)
    print(iframe)
    modal = False
    for l in ls:
        l.prio = Promesse.objects.filter(liste=l, estUnePriorite=True)
    if formS.is_valid() and 'signaler' in request.POST :
        email = formS.cleaned_data['email']
        comment = formS.cleaned_data['comment']
        inform = formS.cleaned_data['inform']
        villeContact = get_object_or_404(Ville, url=url)
        c = Contact(email=email, comment=comment, source='SIN', resteInforme=inform, ville=villeContact)
        c.save()
        modalSignal = True
    if formI.is_valid() and 'formI' in request.POST :
        email = formI.cleaned_data['email']
        villeContact = get_object_or_404(Ville, url=url)
        c = Contact(email=email, ville=villeContact, source='VSL')
        c.save()
        return accueil(request, modal=True)
    if formR.is_valid() and 'formR' in request.POST : #Formulaire rester informé depuis ville avec listes
        email = formI.cleaned_data['email']
        villeContact = get_object_or_404(Ville, url=url)
        c = Contact(email=email, ville=villeContact, source='VAL')
        c.save()
        modalFollow = True
    if formC.is_valid() and 'formC' in request.POST :
        listes=request.POST.getlist('Listes',default=None)
        return compare(request, url, listes=listes)
    return render(request, 'compare/ville.html', locals())

def villeIframe(request, url):
    return ville(request,url, iframe=False)


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
    verif = (datetime.strptime("08/02/2020", "%d/%m/%Y") - datetime.now()).days
    premier = (datetime.strptime("16/03/2020", "%d/%m/%Y") - datetime.now()).days
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
        comment = formC.cleaned_data['comment']
        inform = formC.cleaned_data['inform']
        c = Contact(email=email, comment=comment, source='ACC', resteInforme=inform)
        c.save()
        modal = True
    return render(request, 'compare/accueil.html', locals())


def test(request):
    vs = Ville.objects.all()
    for v in vs:
        v.url = v.nom.replace(" ","").replace("é","e").replace("ô","o").replace("è","e").replace("î","i")
        v.save()
    return render(request, 'compare/testold.html', locals())


