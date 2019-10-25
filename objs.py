import pygame, sys, time, random
from pygame import *
from pygame.sprite import *


#shorthand for scaling while loading image
def image_scaler(img, width, height):
  return pygame.transform.scale((\
    pygame.image.load(img)),\
    (width, height))


#true if everything in the list is the same as the given element,
#in this case a given letter, 'x' or 'o'
def list_same(li, let):
  return all(obj == let for obj in li)


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

  for row in rows:
    if list_same(row, let):
      return True

  return False

#row_match([str(x) for x in range(0, 9)], ' ')


"""
    0 1 2
    3 4 5
    6 7 8
"""


#contains settings for a game
class Config:
  def __init__(self):
    self.alt_settings = False
    self.screen_size = (800, 600)
    self.let_size = (40, 40)
    self.bg_color = (0, 0, 0)
    self.o_color = (128, 159, 255)
    self.x_color = (255, 0, 0)
    self.o_color_alt = (255, 255, 0)
    self.x_color_alt = (102, 0, 102)
    self.grid_color = (166, 166, 166)
    self.text_color = (255, 255, 255)


#contains all stats used by game objs
class Stats:
  def __init__(self):
    self.active = False
    self.o_wins = 0
    self.x_wins = 0
  
  def reset(self):
    self.o_wins = 0
    self.x_wins = 0


class Board(Sprite):
  def __init__(self, config, screen, stats):
    super().__init__()
    self.config = config
    self.screen = screen
    self.stats = stats
    self.screen_rect = screen.get_rect()
    self.image = image_scaler('images/ship.png', 200, 200)
    self.rect = self.image.get_rect()
    self.grid = [' ']*9

  def place(self, pos, let):
    self.grid[pos] = let

  def check(self, let):
    win = False
    
    if row_match(self.grid, 'x'):
      win = True
      self.stats.x_wins += 1

    elif row_match(self.grid, 'o'):
      win = True
      self.stats.o_wins += 1

    return win

  def blitme(self):
    self.screen.blit(self.image, self.rect)

