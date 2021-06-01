import pygame
from utilities.projectile import Projectile
from utilities.animation import AnimateSprite


class Player(AnimateSprite):
	
	def __init__(self, game):
		super().__init__('player')
		self.game = game
		self.health = 150
		self.max_health = 150
		# Puissance d'attaque
		self.attack = 30
		# Vitesse de deplacement du joueur
		self.velocity = 5
		# Redimmensionner l'image du joueur
		self.image = pygame.transform.scale(self.image, (130, 130))
		# Coordonnées du joueur
		self.rect = self.image.get_rect()
		self.rect.x = 50
		self.rect.y = 470
		# Le groupe de projectiles lancés
		self.all_projectiles = pygame.sprite.Group()


	def update_animation(self):
		self.animate()


	def launch_projectile(self):
		"""
			Lancer un projectile
		"""
		self.all_projectiles.add(Projectile(self))
		# Activer l'animation du joueur
		self.start_aniamtion()

		# Jouer le son
		self.game.sound_manager.play('tir')



	def update_health_bar(self, surface):
		"""
			Mettre à jour la jauge de vie des monstres en fonction
			des dégâts subis par ceux-ci
		"""
		# Dessiner les différentes jauges
		pygame.draw.rect(
			surface, 
			(98, 96, 96), 
			[self.rect.x - 10, self.rect.y, self.max_health, 5]
		)
		pygame.draw.rect(
			surface, 
			(0, 0, 255), 
			[self.rect.x - 10, self.rect.y, self.health, 5]
		)


	def damage(self, amount):
		"""
			Infliger des dégâts au joueur en fonction des projectiles
			qu'il aura reçus
		"""
		if self.health - amount > amount:
			self.health -= amount
		else:
			# Si le joueur n'a plus de point de vie
			self.game.game_over()



	"""
		Gérer les déplacements à l'aide de touches du clavier
		Les déplacementsne seront effectifs que si le joueur n'set pas
		en collision avec d'autres éléments(monstres, aliens, ...)
	"""
	def move_up(self):
		self.rect.y -= self.velocity
	def move_down(self):
		self.rect.y += self.velocity
	def move_right(self):
		if not self.game.check_collision(self, self.game.all_monsters):
			self.rect.x += self.velocity
	def move_left(self):
		if not self.game.check_collision(self, self.game.all_monsters):
			self.rect.x -= self.velocity
