import pygame, sys, time, random
from pygame import *
from pygame.sprite import *


#shorthand for scaling while loading image
def image_scaler(img, size):
  return pygame.transform.scale((pygame.image.load(img)), size)


#true if a single row matches
def row_match(li, let):
  rows = [li[0:7:3],
          li[1:8:3],
          li[2:9:3],
          li[0:9:4],
          li[2:7:2],
          li[0:3],
          li[3:6],
          li[6:9]]
  #print(*rows, sep = '\n')

  #true if everything in the list is the same as the given
  for row in rows:
    if all(obj == let for obj in row):
      return True

  return False


#row_match([str(x) for x in range(0, 9)], ' ')
# 0 1 2
# 3 4 5
# 6 7 8
#fxn should iterate over every possible row


def events(config, board):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        sys.exit()