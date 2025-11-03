import pygame

pygame.init()
SCREEN_WIDTH,SCREEN_HEIGHT = 500,500

display_surface=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

background_image=pygame.transform.scale(
    pygame.image.load('background png').convert(),
    (SCREENT_WIDTH,SCREEN_HEIGHT))
penguin_image=pygame.transform.scale(
    pyggame.image.load('hello.peguin.png').convert_alpha(),(200,200))
    pwnguin_rect=penguin_image.get_rect(center=(SCREEN_WIDTH//2,
    SCREEN_HEIGHT //2-30))