from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ListForm, CustomUserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required
from compare.views import liste, accueil
from compare.models import Liste, Ville, Critere, Categorie, Promesse
from django.contrib.auth.decorators import login_required

# New registration form created from scratch
def connect(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Le compte a été crée {username}!  \n'
                                      f'Tu peux te connecter maintenant :)')
            return redirect('')
    else:
        form = CustomUserCreationForm()

    if request.method =='POST':
        form1 = LoginForm(request.POST or None)
        if form.is_valid():
            pass
        return redirect('profile')
    else:
        form1 = LoginForm()

    return render(request, 'users/connect.html', {'form': form, 'form1': form1})


@login_required
def profile(request) :
    return render(request,'users/profile.html')

@login_required
def nouvelleListe(request) :
    form = ListForm(request.POST)
    if form.is_valid():
        l = form.save()
        return redirect(propositions, l.id)
    return render(request,'Users/newList.html', locals())

@login_required
def propositions(request, listeId) :
    l = get_object_or_404(Liste, id=listeId)
    user = request.user
    if user not in l.auteur.all() :
        return redirect('/')
    cats = Categorie.objects.all()
    for c in cats:
        c.crits=[]
        c.crits.extend(Critere.objects.filter(Ville=l.ville, categorie=c))
        for crit in c.crits:
            crit.pro = Promesse.objects.filter(critere=crit, liste=l).first()
    if 'save' in request.POST:
        for cat in cats:
            for cri in cat.crits:
                p = Promesse.objects.filter(critere=crit, liste=l).first()
                if p is not None:
                    p.titre=request.POST.get(str(cri.id), default=None)
                    p.save()
                    pro=Promesse.objects.filter(critere=crit, liste=l).first()
                    print(pro)
                else :
                    p = Promesse(liste=l,titre=request.POST.get(str(cri.id), default=None), critere=cri)
                    p.save()
        return redirect(liste,l.id)
    return render(request,'Users/promesses.html', locals())

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