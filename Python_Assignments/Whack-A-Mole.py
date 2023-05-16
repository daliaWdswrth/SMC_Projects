# -*- coding: utf-8 -*-
"""
Created on Tue May 11 2021
@author: Dalia 
"""


import pygame, random
from pygame.locals import *
from pygame.font import *
from pygame.sprite import *

#Initialize colors
White = ( 255, 255, 255)
Green = ( 0, 155, 0)

pygame.init()
screen = pygame.display.set_mode([640,480])
#Fill screen color
screen.fill(Green)
pygame.display.set_caption("Whack-a-mole")

Width, Height = screen.get_size()


class Mole(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("mole.gif").convert_alpha()
        self.rect = self.image.get_rect()

    #Randomize mole location after hit
    def flee(self):
        x = random.randint(0, Width-1-self.rect.width)
        y = random.randint(0, Height-1-self.rect.height)
        self.rect.topleft = (x,y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Hammer(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("hammer.gif").convert_alpha()
        self.rect = self.image.get_rect()

    #Check if there is a hit
    def hit(self, target):
        return self.rect.colliderect(target)

    #Shovel follow mouse
    def update(self, pt):
        self.rect.center = pt

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def main():
    
    
    #Hide the mouse cursor
    pygame.mouse.set_visible(False)
    
    font = pygame.font.Font(None, 40)
    #Get sound
    Sound = pygame.mixer.Sound('hit.wav')
    Sound.set_volume(1)
    
    
    #Initialize Variables
    hits = 0
    mousePos = (Width/2, Height/2)
    action = False
    
    #Create sprites
    mole = Mole()
    hammer = Hammer()
    
    #Create timer
    clock = pygame.time.Clock()
    counter, text = 10, '10'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    running = True
    while running:
        #Handler events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            #Escape key
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            #Mouse Positioning
            if event.type == MOUSEMOTION:
                mousePos = pygame.mouse.get_pos()
            #Mouse Click
            if event.type == MOUSEBUTTONDOWN:
                action = True
            #Set timer
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else "Time's UP! Press 'Escape' Button" 
            
    
                
        #Update the game
        hammer.update(mousePos)    
        if action:
          action = False
          if hammer.hit(mole):
              Sound.play()
              mole.flee()
              hits += 1
    
    
        #Redraw game
        screen.fill(Green)
        mole.draw(screen)
        hammer.draw(screen)
        
        clock.tick(60)
        #Time Format
        timeIm = font.render(text, True, White)
        screen.blit(timeIm, (10,10))
    
        #Add up number of Hits
        hitCount = font.render("Hits = " + str(hits), True, White)
        #Position hit count
        x = (Width - hitCount.get_width())/1
        y = (Height - hitCount.get_height())/1
        screen.blit(hitCount, (x,y))

        pygame.display.update()
        

main()
pygame.quit()
