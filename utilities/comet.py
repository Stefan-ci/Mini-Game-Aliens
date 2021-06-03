import pygame
import random

class Comet(pygame.sprite.Sprite):

	def __init__(self, comet_event):
		super().__init__()
		self.image = pygame.image.load('assets/comet.png')
		self.image = pygame.transform.scale(self.image, (40, 40))
		self.rect =   self.image.get_rect()

		self.velocity = random.randint(1, 2)
		self.rect.x = random.randint(20, 800)
		self.rect.y = - random.randint(0, 600)

		self.comet_event = comet_event



	def remove(self):
		self.comet_event.all_comets.remove(self)

		# Jouer le son du tomber
		self.comet_event.game.sound_manager.play('meteorite')

		# Vérifier si le nombre de commètes est égal à 0
		if len(self.comet_event.all_comets) == 0:
			# Remettre la barre d'évènement à 0
			self.comet_event.reset_percent()
			# faire reapparaître les 3 premiers monstres
			self.comet_event.game.start()
			

	def fall(self):
		self.rect.y +=  self.velocity

		# Retirer/détruire le commète lorsqu'il touche le sol
		if self.rect.y >= 505:
			self.remove()

			# Vérifier s'il n'y a plus de commètes sur l'écran
			if len(self.comet_event.all_comets) == 0:
				# Réinitialiser la barre d'évènement
				self.comet_event.reset_percent()
				self.comet_event.fall_mode = False


		if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
			# retirer la boule de feu
			self.remove()
			# reduire la jauge de vie du joueur
			self.comet_event.game.player.damage(10)
