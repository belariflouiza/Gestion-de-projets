import unittest
from gestion_taches import GestionTaches

class TestGestionTaches(unittest.TestCase):

    def setUp(self):
        # Initialisation de l'instance de GestionTaches avant chaque test
        self.gestion_taches = GestionTaches()

    def test_ajouter_tache(self):
        # Teste l'ajout d'une tâche et vérifie qu'elle n'est pas complétée initialement
        self.gestion_taches.ajouterTache("Tâche 1", "Description de la tâche 1",2)
        self.assertFalse(self.gestion_taches.verifierTache("Tâche 1"), "La tâche ne devrait pas être complétée initialement.")

    def test_completer_tache(self):
        # Teste l'ajout d'une tâche, la complète, puis vérifie si elle est complétée
        self.gestion_taches.ajouterTache("Tâche 2", "Description de la tâche 2",10)
        self.gestion_taches.completerTache("Tâche 2")
        self.assertTrue(self.gestion_taches.verifierTache("Tâche 2"), "La tâche devrait être complétée.")

    def test_completer_tache_inexistante(self):
        # Teste qu'une KeyError est levée lorsqu'on tente de compléter une tâche qui n'existe pas
        with self.assertRaises(KeyError):
            self.gestion_taches.completerTache("Tâche Inexistante")

    def test_verifier_tache_completee(self):
        # Teste l'ajout d'une tâche, la complète, puis vérifie si elle est complétée
        self.gestion_taches.ajouterTache("Tâche 3", "Description de la tâche 3",8)
        self.gestion_taches.completerTache("Tâche 3")
        self.assertTrue(self.gestion_taches.verifierTache("Tâche 3"), "La tâche devrait être complétée.")

    def test_verifier_tache_non_completee(self):
        # Teste l'ajout d'une tâche et vérifie qu'elle n'est pas complétée
        self.gestion_taches.ajouterTache("Tâche 4", "Description de la tâche 4",4)
        self.assertFalse(self.gestion_taches.verifierTache("Tâche 4"), "La tâche ne devrait pas être complétée.")

    def test_verifier_tache_inexistante(self):
        # Teste qu'une tâche inexistante ne devrait pas exister
        self.assertFalse(self.gestion_taches.verifierTache("Tâche Inexistante"), "La tâche ne devrait pas exister.")
        
    def test_calculer_duree_totale(self):
        # Ajoute quelques tâches avec des durées
        self.gestion_taches.ajouterTache("Tâche 1", "Description de la tâche 1", 5)
        self.gestion_taches.ajouterTache("Tâche 2", "Description de la tâche 2", 10)
        self.gestion_taches.ajouterTache("Tâche 3", "Description de la tâche 3", 7)

        # Complète quelques tâches
        self.gestion_taches.completerTache("Tâche 1")
        self.gestion_taches.completerTache("Tâche 3")

        # Vérifie que la durée totale est correcte (5 + 7)
        self.assertEqual(self.gestion_taches.calculerDureeTotale(), 12, "La durée totale calculée n'est pas correcte.")

if __name__ == '__main__':
    # Exécute les tests si le script est exécuté directement
    unittest.main()
