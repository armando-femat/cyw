from compare.models import Promesse


class vPromesse:
    def __init__(self, l, p):
        self.liste = l
        self.promesse = p


class vCritere:
    def __init__(self, cri, ls):
        self.titre = cri.titre
        self.promesses = []
        for l in ls:
            ps = Promesse.objects.filter(liste=l)
            c=False
            for p in ps:
                if p.critere == cri:
                    self.promesses.append(vPromesse(l, p))
                    c=True
            if c==False:
                self.promesses.append(vPromesse(l, None)) #Si pas de critère pour cette liste

class vCategorie:
    def __init__(self, cat, v, ls):
        self.titre = cat.titre
        self.criteres = []
        for cri in v.criteres.all():
            if cri.categorie==cat:
                self.criteres.append(vCritere(cri, ls))
