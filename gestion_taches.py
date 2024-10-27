class GestionTaches:
    def __init__(self):
        self.taches = {}

    def ajouterTache(self, titre, description, duree):
        self.taches[titre] = {'description': description, 'completee': False, 'duree': duree}

    def completerTache(self, titre):
        if titre in self.taches:
            self.taches[titre]['completee'] = True
        else:
            raise KeyError(f"Tâche '{titre}' non trouvée.")

    def verifierTache(self, titre):
        return titre in self.taches and self.taches[titre]['completee']
    
    def calculerDureeTotale(self):
        return sum(tache['duree'] for tache in self.taches.values() if tache['completee'])