import Modele
import time

class ControleurCourbes(object):
    """ Gere un ensemble de courbes. """
    def __init__(self):
        self.courbes = []

    def ajouterCourbe(self, courbe):
        """ Ajoute une courbe supplementaire. 
        Fonction interne. Utiliser plutot nouvelleDroite... """
        self.courbes.append(courbe) 

    def dessiner(self, dessinerControle, dessinerPoint):
        """ Dessine les courbes. """
        # dessine les point de la courbe
        for courbe in self.courbes:
            courbe.dessinerPoints(dessinerPoint)
        # dessine les point de controle
        for courbe in self.courbes:
            couleur_courbe = courbe.couleur  # Récupère la couleur spécifique de la courbe
            courbe.dessinerControles(dessinerControle)


    

    def nouvelleVerticale(self):
        """ Ajoute une nouvelle verticale initialement vide. 
        Retourne une fonction permettant d'ajouter les points de controle. """
        verticale = Modele.Verticale()
        self.ajouterCourbe(verticale)
        return verticale.ajouterControle

    def nouvelleHorizontale(self):
        """ Ajoute une nouvelle horizontale initialement vide. 
        Retourne une fonction permettant d'ajouter les points de controle. """
        horizontale = Modele.Horizontale()
        self.ajouterCourbe(horizontale)
        return horizontale.ajouterControle
    
    def nouvelleDroite(self):
        """ Ajoute une nouvelle horizontale initialement vide. 
        Retourne une fonction permettant d'ajouter les points de controle. """
        droite = Modele.Droite()
        self.ajouterCourbe(droite)
        return droite.ajouterControle


    def nouvelleCourbeMatrice(self):
        courbe = Modele.CourbeMatrice()
        self.ajouterCourbe(courbe)
        return courbe.ajouterControle

    def nouvelleCourbeDeveloppee(self):
        courbe = Modele.CourbeDeveloppee()
        self.ajouterCourbe(courbe)
        return courbe.ajouterControle
    
    def nouvelleCourbeCasteljau(self):
        courbe = Modele.CourbeDeCasteljau()
        self.ajouterCourbe(courbe)
        return courbe.ajouterControle




