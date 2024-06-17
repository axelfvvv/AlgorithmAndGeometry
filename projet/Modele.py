import numpy as np
import time
import random

class Courbe(object):
    """ Classe generique definissant une courbe. """
    
    def __init__(self):
        self.controles = []
        self.StartTime = 0
        self.EndTime = 0
        self.couleur = '#' + ''.join(random.choice('0123456789ABCDEF') for _ in range(6))

        self.EtatTrace = False
        self.couleurModifié = False


    def dessinerControles(self, dessinerControle):
        """ Dessine les points de controle de la courbe. """
        for controle in self.controles:
            dessinerControle(controle, self.couleur)

    def dessinerPoints(self, dessinerPoint):
        """ Dessine la courbe. Methode a redefinir dans les classes derivees. """
        pass

    def ajouterControle(self, point):
        """ Ajoute un point de controle. """
        self.controles.append(point)

class Horizontale(Courbe):
    """ Definit une horizontale. Derive de Courbe. """                  
                
    def ajouterControle(self, point):
        """ Ajoute un point de controle a l'horizontale.
        Ne fait rien si les 2 points existent deja. """
        if len(self.controles) < 2:
            Courbe.ajouterControle(self, point)

    def dessinerPoints(self, dessinerPoint):
        """ Dessine la courbe. Redefinit la methode de la classe mere. """
        self.StartTime = time.perf_counter()

        if len(self.controles) == 2 :
            x1 = self.controles[0][0]
            x2 = self.controles[1][0]
            y = self.controles[0][1]
            xMin = min(x1,x2)
            xMax = max(x1, x2)
            for x in range(xMin, xMax):
                dessinerPoint((x, y))    
            if(self.EtatTrace == False):
                self.EndTime = time.perf_counter()

                print("Temps d'exécution :  {:.5f}".format(self.EndTime-self.StartTime))
                self.EtatTrace = True


class Verticale(Courbe):
    """ Definit une verticale. Derive de Courbe. """                  
    
    
    def ajouterControle(self, point):
        """ Ajoute un point de controle a la verticale.
        Ne fait rien si les 2 points existent deja. """
        if len(self.controles) < 2:
            Courbe.ajouterControle(self, point)

    def dessinerPoints(self, dessinerPoint):
        """ Dessine la courbe. Redefinit la methode de la classe mere. """
        self.StartTime = time.perf_counter()

        if len(self.controles) == 2 :
            x = self.controles[0][0]
            y1 = self.controles[0][1]
            y2 = self.controles[1][1]
            yMin = min(y1,y2)
            yMax = max(y1, y2)
            for y in range(yMin, yMax):
                dessinerPoint((x, y))   
            if(self.EtatTrace == False):
                self.EndTime = time.perf_counter()

                print("Temps d'exécution :  {:.5f}".format(self.EndTime-self.StartTime))
                self.EtatTrace = True

class Droite(Courbe):         
    
    def ajouterControle(self, point):
        """ Ajoute un point de controle a la verticale.
        Ne fait rien si les 2 points existent deja. """
        if len(self.controles) < 2:
            Courbe.ajouterControle(self, point)

    def dessinerPoints(self, dessinerPoint):
        
        if(len(self.controles) == 2):
            x1 = self.controles[0][0]
            y1 = self.controles[0][1]
            x2 = self.controles[1][0]
            y2 = self.controles[1][1]

            # Calculer la distance entre les points
            distance_x = x2 - x1
            distance_y = y2 - y1
            distance_total = max(abs(distance_x), abs(distance_y))

            # Dessiner des points le long de la ligne reliant les deux points
            for i in range(distance_total + 1):
                # Interpoler les coordonnées du point
                x = x1 + i * distance_x / distance_total
                y = y1 + i * distance_y / distance_total
                # Appeler la méthode dessinerPoint avec les coordonnées du point
                dessinerPoint((x, y))


class CourbeMatrice(Courbe):

    def ajouterControle(self, point):
        """ Ajoute un point de controle a la verticale.
        Ne fait rien si les 2 points existent deja. """
        if len(self.controles) < 4:
            super().ajouterControle(point)


    def _calculerPointsBezierMatrice(self, t_values):
        """ Calcule les points de la courbe de Bézier en utilisant une approche matricielle. """
        t = np.linspace(0, 1, t_values)
        T = np.array([t**3, t**2, t, np.ones_like(t)])
        M = np.array([
            [-1,  3, -3, 1],
            [ 3, -6,  3, 0],
            [-3,  3,  0, 0],
            [ 1,  0,  0, 0]
        ])
        points_controle = np.array(self.controles).T  # Transposer pour que les points soient alignés en colonne
        bezier_points = np.dot(np.dot(points_controle, M), T).T

        return bezier_points.tolist()

    def dessinerPoints(self, dessinerPoint, t_values=1000):
        """ Dessine la courbe. Redefinit la methode de la classe mere. """
        self.StartTime = time.perf_counter()
        """ Dessine la courbe de Bézier. """
        if(len(self.controles) == 4):
            bezier_points = self._calculerPointsBezierMatrice(t_values)
            for point in bezier_points:
                dessinerPoint(point)
            
            if(self.EtatTrace == False):
                self.EndTime = time.perf_counter()
                print("Temps d'exécution :  {:.5f}".format(self.EndTime-self.StartTime))
                self.EtatTrace = True
            

class CourbeDeveloppee(Courbe):

    def ajouterControle(self, point):
        """ Ajoute un point de controle a la verticale.
        Ne fait rien si les 2 points existent deja. """
        if len(self.controles) < 4:
            super().ajouterControle(point)


    def _calculerPointsBezierDeveloppee(self, t_values):
        t = np.linspace(0, 1, t_values)
        T = np.array([(1-t)**3, 3*(1-t)**2*t, 3*(1-t)*t**2, t**3])
        points_controle = np.array(self.controles)

        bezier_points = np.dot(T.T, points_controle)

        return bezier_points.tolist()
    

    def dessinerPoints(self, dessinerPoint, t_values=1000):
        """ Dessine la courbe. Redefinit la methode de la classe mere. """
        self.StartTime = time.perf_counter()
        """ Dessine la courbe de Bézier. """
        if(len(self.controles) == 4):
            bezier_points = self._calculerPointsBezierMatrice(t_values)
            for point in bezier_points:
                dessinerPoint(point)
            
            if(self.EtatTrace == False):
                self.EndTime = time.perf_counter()
                print("Temps d'exécution :  {:.5f}".format(self.EndTime-self.StartTime))
                self.EtatTrace = True
            
class CourbeDeCasteljau(Courbe):

    def ajouterControle(self, point):
        """ Ajoute un point de controle a la verticale.
        Ne fait rien si les 2 points existent deja. """
        if len(self.controles) < 4:
            super().ajouterControle(point)


    def _calculerPointsBezierCasteljau(self, t_values):
        """ Calcule les points de la courbe de Bézier. """
        t = np.linspace(0, 1, t_values)
        bezier_points = np.array([]).reshape(0, 2)  # Créer un tableau vide avec deux colonnes pour stocker les coordonnées (x, y)
        for t_val in t:
            point = self._deCasteljau(t_val)
            bezier_points = np.vstack([bezier_points, point])
        return bezier_points.tolist()
    
    
    def dessinerPoints(self, dessinerPoint, t_values=1000):
        """ Dessine la courbe. Redefinit la methode de la classe mere. """
        self.StartTime = time.perf_counter()
        """ Dessine la courbe de Bézier. """
        if(len(self.controles) == 4):
            bezier_points = self._calculerPointsBezierMatrice(t_values)
            for point in bezier_points:
                dessinerPoint(point)
            
            if(self.EtatTrace == False):
                self.EndTime = time.perf_counter()
                print("Temps d'exécution :  {:.5f}".format(self.EndTime-self.StartTime))
                self.EtatTrace = True
            