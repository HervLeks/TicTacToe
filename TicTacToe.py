#************************ Hervé LEKA & Herman WAKAM *************************#

import pygame
import random

class Jeu:

    def __init__(self):
        self.noir = (0,0,0)
        self.blanc = (255,255,255)
        self.navy = (0,0,128)
        self.size =[600, 600]
        self.abc = False
        self.n = int(input('Entrez le nombre de coups gagnants (3 a 10)'))
        self.termine = False
        self.menubool = True
        while self.abc == False:

        # Le code peut gérer plus de 10*10 cases
        # Pour une utilisation raisonable nous avons ajouter une contrainte a l'utilisateur

            if self.n<3 or self.n>10:
                self.n = int(input('Entrez une valeur valide'))
            else:
                self.abc = True
        self.blockSize = int(600/self.n)
        self.cross = int(self.blockSize/10)
        self.circle = int(self.blockSize/2)

        pygame.init()
        self.fenetre = pygame.display.set_mode(self.size)
        self.horloge = pygame.time.Clock()
        pygame.display.set_caption("Notre Tic Tac Toe")

    def menu(self,message, message_rectangle, couleur):

        font = pygame.font.SysFont('Lato', 30, True)

        message = font.render(message, True, couleur)
        self.fenetre.blit(message, message_rectangle)

    def afficheJeu(self):
        for x in range(int(600/self.blockSize)):
            for y in range(int(600/self.blockSize)):
                rect = pygame.Rect(x*self.blockSize, y*self.blockSize,
                                self.blockSize, self.blockSize)
                pygame.draw.rect(self.fenetre, self.noir, rect, 4)
        self.grille = [[None for a in range(0,self.n)] for b in range(0,self.n)]
    
    def draw(self):
        for y in range(0,len(self.grille)):
            for x in range(0,len(self.grille)):
                if self.grille[y][x] == 'X' :
                    pygame.draw.line(self.fenetre, self.noir, (x * self.blockSize, y * self.blockSize), (self.blockSize + (x * self.blockSize), self.blockSize + (y * self.blockSize)), self.cross)
                    pygame.draw.line(self.fenetre, self.noir, ((x * self.blockSize), self.blockSize + (y * self.blockSize)), (self.blockSize + (x * self.blockSize), (y * self.blockSize)),
                                     self.cross)
                elif self.grille[y][x] == 'O' :
                    pygame.draw.circle(self.fenetre, self.navy, ((self.blockSize/2) + (x * self.blockSize), (self.blockSize/2) + (y * self.blockSize)), self.circle, self.circle//5)

    def ajouterValeur(self,x,y,valeur):
        if self.grille[y][x] == None:
            self.grille[y][x] = valeur

    def viderValeur(self,x,y,valeur):
        self.grille[y][x] = valeur

    def principal(self):
        while self.termine == False and self.abc:
            while self.menubool:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        self.termine = True

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_x:
                            self.choix_utilisateur = 'X'
                            self.menubool = False
                        if event.key == pygame.K_o:
                            self.choix_utilisateur = 'O'
                            self.menubool = False

                self.fenetre.fill(self.blanc)
                self.menu('Notre Tic Tac Toe', [180, 30, 200, 50], self.noir)
                self.menu('Commencer en choisissant/appuyant X ou O',[50, 170, 200, 50], self.noir)
                self.menu('Quitter le jeu : Touche ESCAPE', [100, 350, 200, 50],self.noir)
                self.menu('Revenir au menu: Touche Q ', [130, 450, 200, 50],self.noir)

                pygame.display.flip()
                self.fenetre.fill(self.blanc)
                self.compteur = 0
                self.afficheJeu()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.termine = True
                
                if event.type == pygame.MOUSEBUTTONUP:
                    position = pygame.mouse.get_pos()
                    position_x ,position_y = position[0]//self.blockSize ,position[1]//self.blockSize
                    if self.compteur == 0 :
                        self.ajouterValeur(position_x, position_y, self.choix_utilisateur)
                        self.draw()
                        self.compteur = 1
                        print(self.grille)
                        print("*---*---*---*---*---*---*---*---*---*---*")

                if event.type == pygame.MOUSEMOTION:
                    a = random.randint(0, self.n-1)
                    b = random.randint(0, self.n-1)
                    if self.compteur == 1:
                        if self.grille[b][a] is not None:
                            a = random.randint(0, self.n-1)
                            b = random.randint(0, self.n-1)
                        else:
                            if self.choix_utilisateur == 'X':
                                self.ajouterValeur(a, b, 'O')
                            if self.choix_utilisateur == 'O':
                                self.ajouterValeur(a, b, 'X')
                            self.draw()
                            self.compteur = 0
                            print(self.grille)
                            print("*---*---*---*---*---*---*---*---*---*---*")

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.menubool = True
                        self.restart()

                    if event.key == pygame.K_ESCAPE:
                        self.termine = True

            liste_X = []
            liste_O = []
            liste_lignes_X = []
            liste_colonnes_X = []
            liste_lignes_O = []
            liste_colonnes_O = []
            self.winner(liste_X,liste_O,liste_colonnes_X,liste_lignes_X,liste_lignes_O,liste_colonnes_O)

            pygame.display.flip()
            self.horloge.tick(20)

    def restart(self):
        for ligne in range(0, len(self.grille)):
            for colonne in range(0, len(self.grille)):
                self.viderValeur(colonne, ligne, None)
    
    def winner(self,listeX,listeO,colonnesX,lignesX,lignesO,colonnesO):
        for ligne in range(0, len(self.grille)):
            for colonne in range(0, len(self.grille)):

                if self.grille[ligne][colonne] == 'X':
                    x_pos = (ligne, colonne)
                    listeX.append(x_pos)
                elif self.grille[ligne][colonne] == 'O':
                    o_pos = (ligne, colonne)
                    listeO.append(o_pos)

        if len(listeX) >= self.n:
            for ligne, colonne in listeX:
                lignesX.append(ligne)
                colonnesX.append(colonne)
            for i in range(0, self.n-1):
                if lignesX.count(i) == self.n or colonnesX.count(i) == self.n or lignesX == colonnesX or lignesX == colonnesX[::-1]:
                    self.fenetre.fill(self.blanc)
                    self.compteur = 2
                    if self.choix_utilisateur == 'X':
                        self.menu('Vous avez gagné avec X', [150, 200, 200, 50],self.noir)
                        self.menu('Quitter le jeu : Touche ESCAPE', [100, 350, 200, 50],self.noir)
                        self.menu('Revenir au menu: Touche Q ', [130, 450, 200, 50],self.noir)
                    else:
                        self.menu('L\'ordinateur gagne avec X', [140, 200, 200, 50],self.noir)
                        self.menu('Quitter le jeu : Touche ESCAPE', [100, 350, 200, 50],self.noir)
                        self.menu('Revenir au menu: Touche Q ', [130, 450, 200, 50],self.noir)

        if len(listeO) >= self.n :
            for ligne,collonne in listeO:
                lignesO.append(ligne)
                colonnesO.append(collonne)      
            for j in range(0,self.n-1):
                if lignesO.count(j) == self.n or colonnesO.count(j) == self.n or lignesO == colonnesO or lignesO == colonnesO[::-1]:
                    self.fenetre.fill(self.blanc)
                    self.compteur = 2
                    if self.choix_utilisateur == 'O':
                        self.menu('Vous avez gagné avec O', [150, 200, 200, 50],self.navy)
                        self.menu('Quitter le jeu : Touche ESCAPE', [100, 350, 200, 50],self.noir)
                        self.menu('Revenir au menu: Touche Q ', [130, 450, 200, 50],self.noir)
                    else:
                        self.menu('L\'ordinateur gagne avec O', [140, 200, 200, 50],self.navy)
                        self.menu('Quitter le jeu : Touche ESCAPE', [100, 350, 200, 50],self.noir)
                        self.menu('Revenir au menu: Touche Q ', [130, 450, 200, 50],self.noir)

if __name__ == '__main__':
    pygame.init()
    Jeu().principal()
    pygame.quit()
