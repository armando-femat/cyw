from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import UserRegisterForm, ListForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from compare.views import liste, accueil
from compare.models import Liste, Ville, Critere, Categorie, Promesse
from django.contrib.auth.decorators import login_required


# New registration form created from scratch
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Le compte a été crée {username}!  \n'
                                      f'Tu peux te connecter maintenant :)')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def nouvelleListe(request):
    form = ListForm(request.POST)
    if form.is_valid():
        l = form.save()
        l.auteur.add(request.user)
        l.save()
        return editListe(request, l.id)
    return render(request, 'users/newList.html', locals())


# @login_required
def editListe(request, listeId):
    l = get_object_or_404(Liste, id=listeId)
    user = request.user
    if user not in l.auteur.all():
        return redirect('/')
    cats = Categorie.objects.all()
    for c in cats:
        c.crits = []
        c.crits.extend(Critere.objects.filter(Ville=l.ville, categorie=c))
        for crit in c.crits:
            crit.pro = Promesse.objects.filter(critere=crit, liste=l).first()
    if 'save' in request.POST:
        l.nom = request.POST.get("nom", default=None) if request.POST.get("nom", default=None) != "" else None
        l.teteDeListe = request.POST.get("teteDeListe", default=None) if request.POST.get("teteDeListe",
                                                                                          default=None) != "" else None
        l.presentation = request.POST.get("presentation", default=None) if request.POST.get("presentation",
                                                                                            default=None) != "" else None
        l.couleur = request.POST.get("couleur", default=None) if request.POST.get("couleur",
                                                                                  default=None) != "" else None
        l.lienPhoto = request.POST.get("lienPhoto", default=None) if request.POST.get("lienPhoto",
                                                                                      default=None) != "" else None
        l.site = request.POST.get("site", default=None) if request.POST.get("site", default=None) != "" else None
        l.save()
        prios = request.POST.getlist('prio', default=None)
        for cat in cats:
            for cri in cat.crits:
                p = Promesse.objects.filter(critere=cri, liste=l).first()
                if p is not None:
                    p.titre = request.POST.get(str(cri.id), default=None)
                else:
                    p = Promesse(liste=l, titre=request.POST.get(str(cri.id), default=None), critere=cri)
                if str(p.critere.id) in prios:
                    p.estUnePriorite = True
                else:
                    p.estUnePriorite = False
                p.save()
        return redirect(liste, l.id)
    return render(request, 'users/editListe.html', locals())


""" Old registration form (created with django form)
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Le compte a été crée {username}!  \n'
                                      f'Tu peux te connecter maintenant :)')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
"""
