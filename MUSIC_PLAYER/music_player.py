import pygame
from pygame.locals import *
import os
pygame.init()
screen=pygame.display.set_mode((300,400))
Blue=(173, 216, 230)
screen.fill(Blue)
pygame.display.update()
pygame.display.set_caption("music player")
text_font = pygame.font.SysFont("cambria", 15)

pygame.mixer.init()
music_list=["Mild High Club - Homage.mp3","Hanumankind - Run It Up ( Prod. By Kalmi )  (Official Music Video).mp3","Kendrick Lamar - tv off (Official Audio).mp3","Rarin - Mamacita (Live Performance Video).mp3"]
#sound=pygame.mixer.Sound(music_list[0])


class Button():
    def __init__(self, image, x_pos, y_pos):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        if self.rect.left <= position[0] <= self.rect.right and self.rect.top <= position[1] <= self.rect.bottom:
            return True
        return False

play_button_surface = pygame.image.load("play-button.png")
play_button_surface = pygame.transform.scale(play_button_surface, (50, 50))
next_button_surface= pygame.image.load("next.png")
next_button_surface= pygame.transform.scale(next_button_surface,(50,50))
back_button_surface= pygame.image.load("back.png")
back_button_surface= pygame.transform.scale(back_button_surface,(50,50))

play_button = Button(play_button_surface, 150, 350)
next_button = Button(next_button_surface,250,350)
back_button = Button(back_button_surface,50,350)


def draw_text(text,font,text_col,x,y):
    img=font.render(text,True,text_col)
    screen.blit(img,(x,y))
    
running=True
music_player=False
i=0
while running:
    screen.fill(Blue)
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running=False
		
        if event.type==pygame.MOUSEBUTTONDOWN and play_button.checkForInput(pygame.mouse.get_pos())==True:
            pos=pygame.mouse.get_pos()
            if play_button.checkForInput(pos):
                print("play button")
                if music_player:
                    pygame.mixer.music.stop()
                    music_player=False  
                else:
                    pygame.mixer.music.load(music_list[i])
                    pygame.mixer.music.play()
                    music_player=True
        
        if event.type==pygame.MOUSEBUTTONDOWN and next_button.checkForInput(pygame.mouse.get_pos())==True:
            pos=pygame.mouse.get_pos()
            if next_button.checkForInput(pos):
                print("next button")
                if music_player:
                    pygame.mixer.music.stop()
                    if i>=(len(music_list)-1):
                        i=0
                    else:
                        i+=1
                    pygame.mixer.music.load(music_list[i])
                    pygame.mixer.music.play()
                    music_player=True
        
        if event.type==pygame.MOUSEBUTTONDOWN and back_button.checkForInput(pygame.mouse.get_pos())==True:
            pos=pygame.mouse.get_pos()
            if back_button.checkForInput(pos):
                print("back button")
                if music_player:
                    pygame.mixer.music.stop()
                    if i<=(-1)*(len(music_list)):
                        i=-1
                    else:
                        i-=1
                    pygame.mixer.music.load(music_list[i])
                    pygame.mixer.music.play()
                    music_player=True
    
    
    draw_text(f"Playing: {os.path.splitext(os.path.basename(music_list[i]))[0]}", text_font, (0, 0, 0), 40, 150)
    play_button.update(screen)
    next_button.update(screen)
    back_button.update(screen)
    pygame.display.update()
		
pygame.quit()