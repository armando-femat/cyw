from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from compare.models import Liste, Promesse, Ville
from compare.form import RechercheVille


def liste(request, id):
    l = get_object_or_404(Liste, id=id)
    p = Promesse.objects.filter(liste_id=id)
    return render(request, 'compare/liste.html', {'l': l, 'p': p})


def ville(request, nom):
    v = get_object_or_404(Ville, nom=nom)
    ls = Liste.objects.filter(ville=v)
    return render(request, 'compare/ville.html', locals())


def accueil(request):
    form = RechercheVille(request.POST or None)
    if form.is_valid():
        nom = form.cleaned_data['ville']
        return redirect(ville, nom=nom)

    return render(request, 'compare/accueil.html', locals())


def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = MODEL.objects.filter(name__startswith=q)
        results = []
        print(q)
        for r in search_qs:
            results.append(r.FIELD)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
