import pygame, sys, time, random
from pygame import *


#shorthand for scaling while loading image
def image_scaler(img, width, height):
  return pygame.transform.scale((\
    pygame.image.load(img)),\
    (width, height))


#true if everything in the list is the same
def list_same(li):
  return all(obj == li[0] for obj in li)


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
  def __init__(self, config, screen):
    super().__init__()
    self.screen = screen
    self.screen_rect = screen.get_rect()
    self.image = image_scaler(\
      'images/ship.png', 200, 200)
    self.rect = self.image.get_rect()
    self.grid = [' ']*9

  def place(self, pos, let):
    self.grid[pos] = let

  def check(self, let):
    win = False
    pass

    return win

  def blitme(self):
    self.screen.blit(self.image, self.rect)


def row_match(li, let):
  pass


"""
    0 1 2
    3 4 5
    6 7 8
"""