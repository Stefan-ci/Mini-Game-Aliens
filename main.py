import pygame
import math
from utilities.game import Game

# Initialiser les composants de 'pygame'
pygame.init()

# Définir une clock pour optimiser la vitesse du jeu
clock =   pygame.time.Clock()
FPS = 120 # Une constante (en majuscule)


# Générer la fenêtre de jeu
pygame.display.set_caption('Alien - Shooter')
screen = pygame.display.set_mode((1000, 600))

# Charger l'arrière plan du jeu
background = pygame.image.load('assets/bg.jpg')

# Charger la banière du jeu
banner = pygame.image.load('assets/banner.png')
banner =  pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# Charger le boutton de jeu
play_button =  pygame.image.load('assets/button.png')
play_button =  pygame.transform.scale(play_button, (400, 120))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 1.5)




# Instructions de jeu sur l'écran d'accueil
instructions_header_font = pygame.font.SysFont('monospace', 30, bold=True)
instructions_font = pygame.font.SysFont('fantasy', 30, bold=True, italic=True)

shoot_instruction = "* Touche 'a' : Tirer"
play_instruction = "* Boutton 'play' : Démarrer"
left_instruction = "* Flèche gauche : Aller à gauche"
right_instruction = "* Flèche droite : Aller à droite"

instructions_header_text = instructions_header_font.render(
		'Instructions',
		1,
		(255, 255, 255))
shoot_instruction_text = instructions_font.render(
		shoot_instruction,
		1,
		(255, 255, 255))
play_instruction_text = instructions_font.render(
		play_instruction,
		1,
		(255, 255, 255))
left_instruction_text = instructions_font.render(
		left_instruction,
		1,
		(255, 255, 255))
right_instruction_text = instructions_font.render(
		right_instruction,
		1,
		(255, 255, 255))




# Charger le jeu
game = Game()


# Maintenir la fenêtre de jeu
running = True

while running:

	# Appliquer l'arrière plan du jeu
	screen.blit(background, (0, -300))

	
	# Vérifier si le jeu a débuté
	if game.is_playing:
		# Déclencher les instructions
		game.update(screen)
	else: # Si le jeu n'a pas encore débuté

		# Afficher la banière
		screen.blit(banner, banner_rect)
		# Afficher le boutton 'play'
		screen.blit(play_button, play_button_rect)



		# Afficher les instructions
		screen.blit(instructions_header_text, (30, 20))
		screen.blit(shoot_instruction_text, (40, 60))
		screen.blit(play_instruction_text, (40, 80))
		screen.blit(left_instruction_text, (40, 100))
		screen.blit(right_instruction_text, (40, 120))
						
	




	# Mettre à jour constamment le jeu
	pygame.display.flip()


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
		# Détecter des entrées du clavier (touches)
		elif event.type == pygame.KEYDOWN:
			game.pressed[event.key] = True

			# Détecter si la touche 'espace' est appuyée
				# Si oui, lancer un projectile
				# Sinon, ne rien faire
			if event.key == pygame.K_a:
				if game.is_playing:
					game.player.launch_projectile()
				else:
					game.start() # Lancer le jeu
					game.sound_manager.play('click') # jouer le son

		elif event.type == pygame.KEYUP:
			game.pressed[event.key] = False

		# Vérifier si le jeu a été enclenché à travers le boutton 'play'
		elif event.type == pygame.MOUSEBUTTONDOWN:
			# Si la souris est en collision avec le boutton 'play'
			if play_button_rect.collidepoint(event.pos):
				game.start() # Lancer le jeu
				game.sound_manager.play('click') # jouer le son


	# Fixer le nombre de FPS sur la clock 
	# (pour optimiser la vitesse du jeu)
	clock.tick(FPS)





			


