# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  asteroid_field = AsteroidField()

  Player.containers = (updatable, drawable)
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  Shot.containers = (shots, updatable, drawable)
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    screen.fill("black")

    for sprite in updatable:
      sprite.update(dt)

    for asteroid in asteroids:
      if asteroid.is_colliding(player):
        sys.exit("Game over!")

    for sprite in drawable:
      sprite.draw(screen)

    for shot in shots:
      shot.update(dt)
      shot.draw(screen)
    
    pygame.display.flip()

    # limit the framerate to 60 FPS
    dt = clock.tick(60) / 1000



if __name__ == "__main__":
  main()