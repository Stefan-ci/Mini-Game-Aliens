import pygame
import random
import math
from utilities.comet import Comet


class CometFallEvent:
	"""
		Créer un compteur lors du chargement du jeu
	"""
	def __init__(self, game):
		self.percent = 0
		self.percent_speed = random.randint(4, 5)

		self.all_comets = pygame.sprite.Group() #Groupe de commètes

		self.game = game

		self.fall_mode = False


	def add_percent(self):
		self.percent += self.percent_speed / 100


	def is_full_loaded(self):
		return self.percent >= 100


	def reset_percent(self):
		self.percent = 0


	def attempt_fall(self):
		if self.is_full_loaded() and len(self.game.all_monsters) == 0:
			self.meteor_fall()
			self.fall_mode = True



	def update_bar(self, surface):
		"""
			Une barre de couleur pour la jauge d'évènement
			Une barre noire pour l'arrière plan
		"""
		self.add_percent()

		# Arrière plan
		pygame.draw.rect(surface, (0, 0, 0), [
			0, # x
			surface.get_height() - 10, # y
			surface.get_width(), # largeur de la fenêtre
			10 # épaisseur
			]
		)

		# Barre de couleur pour la jauge d'évènement
		pygame.draw.rect(surface, (187, 11, 11), [
			0, # x
			surface.get_height() - 10, # y
			(surface.get_width() / 100) * self.percent, 
			10 # épaisseur
			]
		)


	def meteor_fall(self):
		for i in range(1, 20):
			self.all_comets.add(Comet(self))