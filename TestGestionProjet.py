# Dans le fichier TestGestionProjet.py
import unittest
from gestion_taches import GestionTaches
from projet import Projet

class TestIntegrationProjet(unittest.TestCase):

    def setUp(self):
        self.gestion_taches = GestionTaches()
        self.projet = Projet("Nom du Projet", self.gestion_taches)

    def test_ajouter_tache_au_projet(self):
        self.projet.ajouterTacheAuProjet("Tâche 3", "Description de la tâche 3",2)
        
        
        print("Gestion Tâches:", self.gestion_taches.taches)
        print("Titres Tâches du Projet:", self.projet.titres_taches)
        self.assertFalse(self.gestion_taches.verifierTache("Tâche 3"), "La tâche ne devrait pas être complétée initialement.")
        self.assertTrue(self.projet.verifierTacheDansProjet("Tâche 3"), "La tâche devrait être ajoutée au projet.")
        

    def test_verifier_tache_dans_projet(self):
        self.projet.ajouterTacheAuProjet("Tâche 2", "Description de la tâche 2",4)
        self.assertTrue(self.projet.verifierTacheDansProjet("Tâche 2"), "La tâche devrait être ajoutée au projet.")
        
    def test_calculer_duree_totale(self):
        
        self.gestion_taches.ajouterTache("Tâche 1", "Description de la tâche 1", 5)
        self.gestion_taches.ajouterTache("Tâche 2", "Description de la tâche 2", 10)
        self.gestion_taches.ajouterTache("Tâche 3", "Description de la tâche 3", 7)

        
        self.gestion_taches.completerTache("Tâche 1")
        self.gestion_taches.completerTache("Tâche 3")

        # Vérifie que la durée totale est correcte (5 + 7)
        self.assertEqual(self.gestion_taches.calculerDureeTotale(), 12, "La durée totale calculée n'est pas correcte.")

if __name__ == '__main__':
    unittest.main()
