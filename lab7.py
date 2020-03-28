import pygame 
pygame.init()

w = 1000
h = 1000

screen = pygame.display.set_mode((w, h))
background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))
background = background.convert()
screen.blit(background, (0,0))

ballsurface = pygame.Surface((1000, 1000))   
pygame.draw.circle(ballsurface, (255, 255, 255), (500,500),500) 
ballsurface = ballsurface.convert() 
#ballx = 320
#bally = 240
screen.blit(ballsurface, (int(w/2) - 500, int(h/2) - 500))

clock = pygame.time.Clock()


activation = True

FPS = 60
playtime = 0.0

while activation:
	milliseconds = clock.tick(FPS)
	playtime += milliseconds/1000
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			activation = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				activation = False

	text = "FPS: {0:.2f} playtime:{1:.2f}".format(clock.get_fps(), playtime)
	pygame.display.set_caption(text)

	pygame.display.flip()

pygame.quit()

print("\nThis game was played for {0:.2f} seconds".format(playtime))