from PhyObjects import MassPoint
import pygame

p1 = MassPoint([20, 20], [0,0], 2, radius=10)
WIN = pygame.display.set_mode((900, 500))
pygame.display.set_caption('Prueba')
clock = pygame.time.Clock()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    WIN.fill((255,255,255))
    p1.draw(WIN, (0,200,200))
    pygame.display.update()