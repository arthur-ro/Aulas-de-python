
# NÃO FUNCIONA MAIS POIS OUVE AUTOALIZAÇÕES
'''import pygame
pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
pygame.event.wait()'''


# ESSA ESTA AUTOALIZADO
import pygame
pygame.mixer.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play(loops=0)
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)






