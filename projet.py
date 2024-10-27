
class Projet:
    def __init__(self, nom, gestion_taches):
        self.nom = nom
        self.gestion_taches = gestion_taches
        self.titres_taches = []

    def ajouterTacheAuProjet(self, titre, description,duree):
        self.gestion_taches.ajouterTache(titre, description,duree)
        self.titres_taches.append(titre)

    def verifierTacheDansProjet(self, titre):
        return titre in self.titres_taches
