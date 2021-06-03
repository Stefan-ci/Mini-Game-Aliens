import pygame
from utilities.player import Player
from utilities.monster import Monster, Mummy, Alien
from utilities.comet_event import CometFallEvent
from utilities.sound import SoundManager


class Game:

	def __init__(self):
		# Définir si le jeu a commencé ou pas
		self.is_playing = False

		self.all_players = pygame.sprite.Group() # Groupe de joueurs
		self.player = Player(self)
		self.all_players.add(self.player)
		self.all_monsters = pygame.sprite.Group() # Groupe de monstres
		self.pressed = {}

		# Score du jeu (0)
		self.score_num_font = pygame.font.SysFont('monospace', 40, bold=True)
		self.socre_text_font = pygame.font.SysFont('monospace', 30, bold=True, italic=True)
		self.score = 0

		# Gérer un sound à chque évènement bien spécifique
		self.sound_manager = SoundManager()


		self.comet_event = CometFallEvent(self)


	def add_score(self, score_points=10):
		self.score += score_points



	def start(self):
		self.is_playing = True
		# Faire apparaître les monstres automatiquement
		self.spawn_monster(Mummy)
		self.spawn_monster(Mummy)
		self.spawn_monster(Alien)




	def update(self, screen):
		# Appliquer l'image du joueur
		screen.blit(self.player.image, self.player.rect)

		# Appliquer les projectiles
		self.player.all_projectiles.draw(screen)

		# Appliquer les monstres
		self.all_monsters.draw(screen)

		# Appliquer les commètes sur l'écran
		self.comet_event.all_comets.draw(screen)

		# Actualiser la barre de vie du joueur
		self.player.update_health_bar(screen)

		# Actualiser l'animation du joueur
		self.player.update_animation() 

		# Actualiser la barre d'évènement du jeu
		self.comet_event.update_bar(screen)

		# Afficher le score sur l'écran et l'actualiser
		"""
			pygame.font.SysFont(name, size, bold=False, italic=False)
		"""
		score_num = self.score_num_font.render(str(self.score), 1, (255, 255, 255))
		socre_text = self.socre_text_font.render('SCORE : ', 1, (255, 255, 255))
		screen.blit(socre_text, (20, 20))
		screen.blit(score_num, (170, 15))


		# Récupérer les projectiles lancés et actionner le deplacement
		for projectile in self.player.all_projectiles:
			projectile.move()


		# Récupérer les monstres et actionner leur deplacement
		for monster in self.all_monsters:
			monster.forward()
			monster.update_health_bar(screen)
			# Actualiser l'animation du monstre
			monster.update_animation() 


		# Récupérer les commètes et actionner leur déplacement
		for comet in self.comet_event.all_comets:
			comet.fall()




		# Vérifier la touche appuyée et actionner le déplacement
		if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
			self.player.move_right()
		elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
			self.player.move_left()
		"""
		elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < screen.get_height():
			self.player.move_down()
		elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
			self.player.move_up()
						
		"""
	def game_over(self):
		"""
			Réinitialiser les composants du jeu
				* Remettre le joueur à neuf
				* Retirer les ennemis
				* Retourner sur la page d'accueil
		"""
		self.all_monsters =  pygame.sprite.Group()
		self.comet_event.all_comets = pygame.sprite.Group()
		self.player.health = self.player.max_health
		self.comet_event.reset_percent()
		self.is_playing = False
		self.score = 0

		# Jouer le son de 'game_over'
		self.sound_manager.play('game_over')


	def spawn_monster(self, monster_class_name):
		self.all_monsters.add(monster_class_name.__call__(self))


	def check_collision(self, sprite, group):
		return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)