# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame

from constants import *
from player import *
from asteroid import*
from asteroidfield import *
from shot import Shot

def main():
   pygame.init()
   
   clock = pygame.time.Clock()
   dt = 0

   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
   #group
   updateable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   all_asteroids = pygame.sprite.Group()
   shots = pygame.sprite.Group()

   Asteroid.containers = (updateable, drawable, all_asteroids)
   Shot.containers = (shots, updateable, drawable)
   AsteroidField.containers = (updateable)

   asteroid_field = AsteroidField()   

   Player.containers = (updateable, drawable)

   player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
 
   
   while True:
   	for event in pygame.event.get():
        	if event.type == pygame.QUIT:
                	return False
   	dt = clock.tick(60) / 1000
   	

   	for obj in updateable:
   		obj.update(dt)

   	screen.fill("black")   	

   	for obj in drawable:
   		obj.draw(screen)

   	for asteroid in all_asteroids:
   		for bullet in shots: 
   			if asteroid.detect_collision(bullet):
   				new_asteroids = asteroid.split()
   				if new_asteroids:
   					all_asteroids.add(new_asteroids)
   	for asteroid in all_asteroids:
   		if player.detect_collision(asteroid):
   			sys.exit("Game over!")   	

   	pygame.display.flip()
   	
if __name__ == "__main__":
   main()
