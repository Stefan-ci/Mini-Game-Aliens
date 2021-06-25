import pygame
import random
from utilities.animation import AnimateSprite



"""
	Il existe différents types de monstres:
		* Les monstres eux-mêmes (momies)
		* Les aliens

	Il faut donc nécessairement une classe pour chaque type de monstres
	Ainsi, elles (classes) pourront hériter de la super classe Monster()
	qui a pour paramètres:
		- game
		- monster_name
		- monster_size
		- offset -> décallage pour le repositionnement d'un monstre
"""





class Monster(AnimateSprite):
	""" La super classe Monster pour tous les monstres """

	def __init__(self, game, monster_name, monster_size, offset=0):
		super().__init__(monster_name, monster_size)
		self.game = game
		self.health = 100
		self.max_health = 100
		self.attack = 0.2
		self.image = pygame.transform.scale(self.image, (130, 130))
		self.rect =  self.image.get_rect()
		self.rect.x = 700 +  random.randint(0, 200)
		self.rect.y = 455 - offset
		# Le nombre de points ajouté au score en fonction du monstre tué 
		self.loot_amount = 10
		self.start_aniamtion()


	def set_speed(self, speed):
		self.default_speed = speed
		self.velocity = random.randint(3, self.default_speed)


	def set_loot_amount(self, amount):
		self.loot_amount = amount


	def forward(self):
		"""
			Faire avancer les monstres vers le joueur
			Les déplacementsne seront effectifs que si le joueur 
			n'set pas en collision avec d'autres éléments
			(monstres, aliens, ...)
		"""
		if not self.game.check_collision(self, self.game.all_players):
			self.rect.x -= self.velocity

		# Si le monstre est en collision avec le joueur
		else:
			# infliger des dégâts au joueur
			self.game.player.damage(self.attack)



	def update_animation(self):
		self.animate(loop=True)



	def update_health_bar(self, surface):
		"""
			Mettre à jour la jauge de vie des monstres en fonction
			des dégâts subis par ceux-ci
		"""
		# Dessiner les différentes jauges
		pygame.draw.rect(
			surface, 
			(98, 96, 96), 
			[self.rect.x + 15, self.rect.y - 20, self.max_health, 5]
		)
		pygame.draw.rect(
			surface, 
			(43, 216, 59), 
			[self.rect.x + 15, self.rect.y - 20, self.health, 5]
		)


	def damage(self, amount):
		"""
			Infliger des dégâts au monstre en fonction des projectiles
			qu'il aura reçus
		"""
		self.health -= amount

		# Vérifier si self.health <= 0. Si oui, le monstre meurt
		# Sinon, il continue de vivre
		if self.health <= 0:
			# Faire reapparaître le monstre comme un nouveau
			self.rect.x = 700 + random.randint(0, 400)
			self.health = self.max_health
			self.velocity = random.randint(1, 2)

			# Incrémenter le score du joueur lorsqu'il tue un monstre
			self.game.add_score(self.loot_amount)

			# Si la barre d'évènement est chargé à 100%, il ne faut plus
			# reapparaître de monstres

			if self.game.comet_event.is_full_loaded():
				self.game.all_monsters.remove(self)


				# Essayer de déclencher la pluie de commètes
				self.game.comet_event.attempt_fall()




""" La classe enfant 'Mummy' pour les momies"""
class Mummy(Monster):

	def __init__(self, game):
		super().__init__(game, 'mummy', (130, 130))
		self.set_speed(8)
		self.set_loot_amount(20)


""" La classe enfant 'Alien' pour les aliens"""
class Alien(Monster):

	def __init__(self, game):
		super().__init__(game, 'alien', (200,  200), 50)

		self.health = 200
		self.max_health = 200
		self.attack = 0.5
		self.set_speed(6)
		self.set_loot_amount(40)

