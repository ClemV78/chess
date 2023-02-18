# A faire : castle et pion sur dernière case = reine et echec (que le roi qui peut bouger)
import pygame
import time
import sys
pygame.init()

size = width, height = 600, 600
black = 0, 0, 0
white = 255, 255, 255
brown = 160, 82, 45
blue = 135, 206, 250
dark_blue = 16, 52, 166
yellow = 255, 255, 80
dark_yellow = 218, 179, 10
green = 173, 255, 47

screen = pygame.display.set_mode(size)
bol_selection = False
position_selection = (0, 0)
piece_selection = None
pion_arrive = False
couleur_en_jeu = 'w'
liste_position_case = []


def addition_couple(l1, l2):
    return((l1[0]+l2[0], l1[1]+l2[1]))


def dedans(couple):
    i, j = couple
    if i < 0 or i > 7:
        return(False)
    if j < 0 or j > 7:
        return(False)
    return(True)

# Définition des pièces


def load_image(img, position, scale=(75, 75)):  # img = "pic.png", position = (75,525)
    img = pygame.image.load(img)
    img = pygame.transform.scale(img, scale)
    img_rect = img.get_rect(topleft=position)
    return(img, img_rect)


class Cavalier:
    def mouvements_possibles_cavalier(self):
        l = []
        # Tout droit
        couples = [(2, 1), (2, -1), (1, 2), (-2, 1),
                   (1, -2), (-1, 2), (-1, -2), (-2, -1)]
        for couple in couples:
            mouvement = addition_couple(self.position, couple)
            if mouvement in liste_position_case:
                # Manger
                if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                    l.append(mouvement)
            else:
                l.append(mouvement)
        return([couple for couple in l if dedans(couple)])

    def __init__(self, fichier, position, couleur='w'):
        self.couleur = couleur
        self.position = position
        self.fichier = fichier
        self.mouvements_possibles = self.mouvements_possibles_cavalier()
        self.image, self.image_rect = load_image(
            fichier, (self.position[0]*75, self.position[1]*75), (75, 75))

    def mouvement(self, nouvelle_position):
        self.position = nouvelle_position
        self.mouvements_possibles = self.mouvements_possibles_cavalier()
        self.image, self.image_rect = load_image(
            self.fichier, (self.position[0]*75, self.position[1]*75), (75, 75))

    def selection(self):
        self.mouvements_possibles = self.mouvements_possibles_cavalier()


class Fou:
    def mouvements_possibles_fou(self):
        l = []
        # Gauche et Bas
        direction = (-1, 1)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        # Droit et Haut
        direction = (1, -1)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        # Droite et Bas
        direction = (1, 1)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        # Gauche et Haut
        direction = (-1, -1)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        return(l)

    def __init__(self, fichier, position, couleur='w'):
        self.couleur = couleur
        self.position = position
        self.fichier = fichier
        self.mouvements_possibles = self.mouvements_possibles_fou()
        self.image, self.image_rect = load_image(
            fichier, (self.position[0]*75, self.position[1]*75), (75, 75))

    def mouvement(self, nouvelle_position):
        self.position = nouvelle_position
        self.mouvements_possibles = self.mouvements_possibles_fou()
        self.image, self.image_rect = load_image(
            self.fichier, (self.position[0]*75, self.position[1]*75), (75, 75))

    def selection(self):
        self.mouvements_possibles = self.mouvements_possibles_fou()


class Reine:
    def mouvements_possibles_reine(self):
        l = []
        # Gauche et Bas
        direction = (-1, 1)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        # Droit et Haut
        direction = (1, -1)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        # Droite et Bas
        direction = (1, 1)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        # Gauche et Haut
        direction = (-1, -1)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        # Bas
        direction = (0, 1)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        # Haut
        direction = (0, -1)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        # Droite
        direction = (1, 0)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        # Gauche
        direction = (-1, 0)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)
        return(l)

    def __init__(self, fichier, position, couleur='w'):
        self.couleur = couleur
        self.position = position
        self.fichier = fichier
        self.mouvements_possibles = self.mouvements_possibles_reine()
        self.image, self.image_rect = load_image(
            fichier, (self.position[0]*75, self.position[1]*75), (75, 75))

    def mouvement(self, nouvelle_position):
        self.position = nouvelle_position
        self.mouvements_possibles = self.mouvements_possibles_reine()
        self.image, self.image_rect = load_image(
            self.fichier, (self.position[0]*75, self.position[1]*75), (75, 75))

    def selection(self):
        self.mouvements_possibles = self.mouvements_possibles_reine()


class Roi:
    def mouvements_possibles_roi(self):
        l = []
        # Tout droit
        couples = [(0, 1), (0, -1), (1, -1), (1, 1),
                   (1, 0), (-1, 1), (-1, -1), (-1, 0)]
        for couple in couples:
            mouvement = addition_couple(self.position, couple)
            if mouvement in liste_position_case:
                # Manger
                if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                    l.append(mouvement)
            else:
                l.append(mouvement)

        # Castle
        if self.premier_mouv:
            if self.couleur == 'w':
                if blanc_tour_droite.premier_mouv:
                    cases_a_liberer = [(5, 7), (6, 7)]
                    if cases_a_liberer[0] not in liste_position_case and cases_a_liberer[1] not in liste_position_case:
                        l.append((6, 7))
            else:
                if noir_tour_droite.premier_mouv:
                    cases_a_liberer = [(5, 0), (6, 0)]
                    if cases_a_liberer[0] not in liste_position_case and cases_a_liberer[1] not in liste_position_case:
                        l.append((6, 0))

        return([couple for couple in l if dedans(couple)])

    def __init__(self, fichier, position, couleur='w'):
        self.couleur = couleur
        self.position = position
        self.premier_mouv = True
        self.fichier = fichier
        self.mouvements_possibles = self.mouvements_possibles_roi()
        self.image, self.image_rect = load_image(
            fichier, (self.position[0]*75, self.position[1]*75), (75, 75))

    def mouvement(self, nouvelle_position):
        self.position = nouvelle_position
        if self.premier_mouv and nouvelle_position == (6, 7):  # castle white
            blanc_tour_droite.mouvement((5, 7))
        if self.premier_mouv and nouvelle_position == (6, 0):  # castle black
            noir_tour_droite.mouvement((5, 0))

        self.premier_mouv = False
        self.mouvements_possibles = self.mouvements_possibles_roi()
        self.image, self.image_rect = load_image(
            self.fichier, (self.position[0]*75, self.position[1]*75), (75, 75))

    def selection(self):
        self.mouvements_possibles = self.mouvements_possibles_roi()


class Tour:
    def mouvements_possibles_tour(self):
        l = []
        # Bas
        direction = (0, 1)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        # Haut
        direction = (0, -1)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        # Droite
        direction = (1, 0)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        # Gauche
        direction = (-1, 0)
        mouvement = addition_couple(self.position, direction)
        while mouvement not in liste_position_case and dedans(mouvement):
            l.append(mouvement)
            mouvement = addition_couple(mouvement, direction)
        if mouvement in liste_position_case:
            # Manger
            if pieces[liste_position_case.index(mouvement)].couleur != self.couleur:
                l.append(mouvement)

        return(l)

    def __init__(self, fichier, position, couleur='w'):
        self.couleur = couleur
        self.position = position
        self.premier_mouv = True
        self.fichier = fichier
        self.mouvements_possibles = self.mouvements_possibles_tour()
        self.image, self.image_rect = load_image(
            fichier, (15+self.position[0]*75, 4+self.position[1]*75), (55, 70))

    def mouvement(self, nouvelle_position):
        self.position = nouvelle_position
        self.premier_mouv = False
        self.mouvements_possibles = self.mouvements_possibles_tour()
        self.image, self.image_rect = load_image(
            self.fichier, (15+self.position[0]*75, 4+self.position[1]*75), (55, 70))

    def selection(self):
        self.mouvements_possibles = self.mouvements_possibles_tour()


class Pion:
    def mouvements_possibles_pion(self):
        l = []
        # Tout droit
        if self.couleur == 'w':
            couple = (0, -1)
            tout_droit = addition_couple(self.position, couple)
            if tout_droit not in liste_position_case:
                l.append(tout_droit)
                if self.premier_mouv:
                    loin = addition_couple(self.position, (0, -2))
                    if loin not in liste_position_case:
                        l.append(loin)

        else:
            couple = (0, 1)
            tout_droit = addition_couple(self.position, couple)
            if tout_droit not in liste_position_case:
                l.append(tout_droit)
                if self.premier_mouv:
                    loin = addition_couple(self.position, (0, 2))
                    if loin not in liste_position_case:
                        l.append(loin)

        # Manger
        if self.couleur == 'w':
            couple1 = (1, -1)
            couple2 = (-1, -1)
        else:
            couple1 = (1, 1)
            couple2 = (-1, 1)
        manger_droite = addition_couple(self.position, couple1)
        manger_gauche = addition_couple(self.position, couple2)
        if manger_droite in liste_position_case:
            if pieces[liste_position_case.index(manger_droite)].couleur != self.couleur:
                l.append(manger_droite)
        if manger_gauche in liste_position_case:
            if pieces[liste_position_case.index(manger_gauche)].couleur != self.couleur:
                l.append(manger_gauche)

        # arrivée à la dernière case
        if self.couleur == 'w' and self.position[1] == 0:
            l.append((self.position[0], 1))
            l.append((self.position[0], 2))
            pieces.append()
        elif self.couleur == 'b' and self.position[1] == 7:
            l.append((self.position[0], 6))
            l.append((self.position[0], 5))

        return([couple for couple in l if dedans(couple)])

    def __init__(self, fichier, position, couleur='w'):
        self.couleur = couleur
        self.position = position
        self.fichier = fichier
        self.premier_mouv = True
        self.mouvements_possibles = self.mouvements_possibles_pion()
        self.image, self.image_rect = load_image(
            fichier, (10+self.position[0]*75, 10+self.position[1]*75), (45, 60))

    def mouvement(self, nouvelle_position):
        global pion_arrive
        if self.couleur == 'w' and self.position[1] == 0:
            pion_arrive = True
            # nouvelle reine blanche
            if nouvelle_position == (self.position[0], 1):
                self.__class__ = Reine
                self.__init__("blanc_reine.png", self.position)
            # nouveau cavalier blanc
            elif nouvelle_position == (self.position[0], 2):
                self.__class__ = Cavalier
                self.__init__("blanc_cavalier_droit.png", self.position)

        elif self.couleur == 'b' and self.position[1] == 7:
            pion_arrive = True
            # nouvelle reine noire
            if nouvelle_position == (self.position[0], 6):
                self.__class__ = Reine
                self.__init__("noir_reine.png", self.position, 'b')
            # nouveau cavalier noire
            elif nouvelle_position == (self.position[0], 5):
                self.__class__ = Cavalier
                self.__init__("noir_cavalier_droit.png", self.position, 'b')
        else:
            self.position = nouvelle_position
            self.premier_mouv = False
            self.mouvements_possibles = self.mouvements_possibles_pion()
            self.image, self.image_rect = load_image(
                self.fichier, (10+self.position[0]*75, 10+self.position[1]*75), (45, 60))
         #print(pion_arrive)

    def selection(self):
        self.mouvements_possibles = self.mouvements_possibles_pion()


# blanc
blanc_cavalier_droit = Cavalier(
    "images/blanc_cavalier_droit.png", (1, 7))
blanc_cavalier_gauche = Cavalier(
    "images/blanc_cavalier_gauche.png", (6, 7))
blanc_fou_droit = Fou(
    "images/blanc_fou.png", (2, 7))
blanc_fou_gauche = Fou(
    "images/blanc_fou.png", (5, 7))
blanc_tour_droite = Tour(
    "images/blanc_tour.png", (7, 7))
blanc_tour_gauche = Tour(
    "images/blanc_tour.png", (0, 7))
blanc_reine = Reine(
    "images/blanc_reine.png", (3, 7))
blanc_roi = Roi("images/blanc_roi.png", (4, 7))
blanc_pion1 = Pion(
    "images/blanc_pion.png", (0, 6))
blanc_pion2 = Pion(
    "images/blanc_pion.png", (1, 6))
blanc_pion3 = Pion(
    "images/blanc_pion.png", (2, 6))
blanc_pion4 = Pion(
    "images/blanc_pion.png", (3, 6))
blanc_pion5 = Pion(
    "images/blanc_pion.png", (4, 6))
blanc_pion6 = Pion(
    "images/blanc_pion.png", (5, 6))
blanc_pion7 = Pion(
    "images/blanc_pion.png", (6, 6))
blanc_pion8 = Pion(
    "images/blanc_pion.png", (7, 6))

# noir
noir_cavalier_droit = Cavalier(
    "images/noir_cavalier_droit.png", (1, 0), 'b')
noir_cavalier_gauche = Cavalier(
    "images/noir_cavalier_gauche.png", (6, 0), 'b')
noir_fou_droit = Fou(
    "images/noir_fou.png", (2, 0), 'b')
noir_fou_gauche = Fou(
    "images/noir_fou.png", (5, 0), 'b')
noir_tour_droite = Tour(
    "images/noir_tour.png", (7, 0), 'b')
noir_tour_gauche = Tour(
    "images/noir_tour.png", (0, 0), 'b')
noir_reine = Reine("images/noir_reine.png", (3, 0), 'b')
noir_roi = Roi("images/noir_roi.png", (4, 0), 'b')
noir_pion1 = Pion(
    "images/noir_pion.png", (0, 1), 'b')
noir_pion2 = Pion(
    "images/noir_pion.png", (1, 1), 'b')
noir_pion3 = Pion(
    "images/noir_pion.png", (2, 1), 'b')
noir_pion4 = Pion(
    "images/noir_pion.png", (3, 1), 'b')
noir_pion5 = Pion(
    "images/noir_pion.png", (4, 1), 'b')
noir_pion6 = Pion(
    "images/noir_pion.png", (5, 1), 'b')
noir_pion7 = Pion(
    "images/noir_pion.png", (6, 1), 'b')
noir_pion8 = Pion(
    "images/noir_pion.png", (7, 1), 'b')
pieces = [blanc_cavalier_droit, blanc_cavalier_gauche, blanc_fou_droit, blanc_fou_gauche, blanc_reine, blanc_roi, blanc_tour_droite, blanc_tour_gauche, blanc_pion1, blanc_pion2, blanc_pion3, blanc_pion4, blanc_pion5, blanc_pion6, blanc_pion7, blanc_pion8,
          noir_cavalier_droit, noir_cavalier_gauche, noir_fou_droit, noir_fou_gauche, noir_reine, noir_roi, noir_tour_droite, noir_tour_gauche, noir_pion1, noir_pion2, noir_pion3, noir_pion4, noir_pion5, noir_pion6, noir_pion7, noir_pion8]

# Définition du plateau
liste_position_case = [piece.position for piece in pieces]

while 1:

    def affichage(selection=(False, (0, 0))):
        # Affichage plateau
        screen.fill(brown)
        for i in range(8):
            for j in range(4):
                pygame.draw.rect(
                    screen, white, (75*i, 75*2*j+75*(i % 2), 75, 75))

        if selection[0]:
            i, j = selection[1]
            pygame.draw.rect(
                screen, dark_blue, (75*i, 75*j, 75, 75))
            pygame.draw.rect(
                screen, blue, (75*i+1, 75*j+1, 73, 73))
            for i, j in piece_selection.mouvements_possibles:
                pygame.draw.rect(
                    screen, dark_yellow, (75*i, 75*j, 75, 75))
                pygame.draw.rect(
                    screen, yellow, (75*i+1, 75*j+1, 73, 73))

        for piece in pieces:
            screen.blit(piece.image, piece.image_rect)
        pygame.display.flip()

    affichage(selection=(bol_selection, position_selection))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()

            # Définition du plateau

            if bol_selection:
                # selection d'une nouvelle position

                if (x//75, y//75) in piece_selection.mouvements_possibles:  # selection de la case où bouger
                    bol_selection = False
                    piece_selection.mouvement((x//75, y//75))

                    if not pion_arrive:  # pas le changement d'un pion pour une autre piece à la fin de l'échequier
                        if (x//75, y//75) in liste_position_case:  # Mange
                            indice_mangee = liste_position_case.index(
                                (x//75, y//75))
                            piece_mangee = pieces[indice_mangee]
                            pieces.pop(indice_mangee)
                            if piece_mangee in [noir_roi, blanc_roi]:  # Fin de la partie
                                print("OVER")
                        liste_position_case = [
                            piece.position for piece in pieces]

                        if couleur_en_jeu == 'w':
                            couleur_en_jeu = 'b'
                        else:
                            couleur_en_jeu = 'w'
                    else:
                        pion_arrive = False
                elif (x//75, y//75) in liste_position_case and pieces[liste_position_case.index(
                        (x//75, y//75))].couleur == couleur_en_jeu:  # selection d'une autre pièce de la couleur en jeu
                    position_selection = (x//75, y//75)
                    piece_selection = pieces[liste_position_case.index(
                        (x//75, y//75))]
                    piece_selection.selection()

            else:
                if (x//75, y//75) in liste_position_case and pieces[liste_position_case.index(
                        (x//75, y//75))].couleur == couleur_en_jeu:  # selection d'une pièce de la couleur en jeu
                    bol_selection = True
                    position_selection = (x//75, y//75)
                    piece_selection = pieces[liste_position_case.index(
                        (x//75, y//75))]
                    piece_selection.selection()
