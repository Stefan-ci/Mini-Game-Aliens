import pygame

class Projectile(pygame.sprite.Sprite):

	def __init__(self, player):
		super().__init__()
		self.velocity = 5
		self.player = player
		self.image = pygame.image.load('assets/projectile.png')
		# Redimmensionner l'image du projectile
		self.image = pygame.transform.scale(self.image, (30, 30))
		# Coordonnées du projectile
		self.rect = self.image.get_rect()
		# Placer le projectile au même niveau que le joueur
		# 105px & 55px ont été ajoutées de façon proportionnelle
		self.rect.x = player.rect.x + 130
		self.rect.y = player.rect.y + 50
		# Ci-dessous, les atributs pour la rotation des projectiles
		self.origin_image = self.image
		self.angle = 0 # angle de rotation du projectile


	def remove(self):
		"""
			Détruire le projectile s'il n'est sur l'écran
		"""
		self.player.all_projectiles.remove(self)


	def move(self):
		"""
			Déplacer le projectile
		"""
		self.rect.x += self.velocity
		self.rotate()

		# Vérifier si le projectile est entré en collision avec
		# un monstre, alors il faut supprimer ledit projectile
		# pour ne pas qu'il tue aussi tous les autres monstres
		for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
			self.remove()
			monster.damage(self.player.attack)


		# supprimer le projectile une fois qu'il aura traversé 
		# la largeur de l'écran (s'il n'a touché aucun monstre)
		if self.rect.x > 970:
			self.remove()


	def rotate(self):
		"""
			Faire tourner le projectile sur lui-même
			pour un effet de rotation lors du déplacement
		"""
		self.angle += 3
		self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
		self.rect =  self.image.get_rect(center=self.rect.center)