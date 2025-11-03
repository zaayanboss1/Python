import pygame

pygame.init()
pygame.display.set_mode((500,400))
done=False
while not done:
    for i in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.flip