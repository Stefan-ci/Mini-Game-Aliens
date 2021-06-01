import pygame

class AnimateSprite(pygame.sprite.Sprite):

	def __init__(self, sprite_name, monster_size=(130, 130)):
		super().__init__()
		self.monster_size = monster_size
		# Charger l'image de façon générique avec 'sprite_name'
		self.image = pygame.image.load(f'assets/{sprite_name}.png')
		self.image = pygame.transform.scale(self.image, monster_size)
		self.current_image = 0 # L'animation commence par la 1ère image

		self.images = animations.get(sprite_name)

		self.animation = False



	def start_aniamtion(self):
		"""
			Méthode pour démarrer l'animation lorsqu'une action
			est enclenchée
		"""
		self.animation = True



	def animate(self, loop=False):
		"""
			Définir une méthode pour animer le sprite
		"""

		# Vérifier si l'animation est active
		if self.animation: # if self.animation is True:
			self.current_image += 1 # Passer à l'image suivante
			# Vérifier si la fin de l'animation est atteinte (dernière image)
			if self.current_image >= len(self.images):
				self.current_image = 0 # Remettre l'animation de départ

				# Vérifier si l'animation n'est pas en mode boucle
				if loop is False:
					self.animation = False # Arrêter l'animation

			# Remplacer une image par la suivante
			self.image = self.images[self.current_image]
			self.image = pygame.transform.scale(self.image, self.monster_size)





def load_aniamtion_images(sprite_name):
	"""
		Charger les images d'un sprite/d'une entité
	"""
	# Charger les 24 images de chaque entité
	images = []

	# Récupérer le chemin du dossier dudit sprite
	path = f"assets/{sprite_name}/{sprite_name}"

	# Boucle pour lire chaque image () du dossier 'sprite_name'
	for num in range(1, 24):
		image_path = path + str(num) + '.png'
		# Ajouter un composant à la liste 'images'
		images.append(pygame.image.load(image_path))

	# Retourner le contenu de 'images'
	return images




# Contient les images chargées de chaque sprite
# Type : dict
animations = {
	'mummy' : load_aniamtion_images('mummy'),
	'alien' : load_aniamtion_images('alien'),
	'player' : load_aniamtion_images('player'),
}


