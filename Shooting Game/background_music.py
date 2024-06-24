import pygame
pygame.init()


class Music:
    def playing():
        pygame.mixer.music.load('IGI_background.mp3')
        pygame.mixer.music.play(-1)

    def gun_shot():
        pygame.mixer.music.load('gun_shot.mp3')
        pygame.mixer.music.play(0)
    
    def men_shot():
        pygame.mixer.music.load('men_shot.mp3')
        pygame.mixer.music.play(0)        
