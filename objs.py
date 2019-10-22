import pygame, sys, time
from pygame import *

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


class Board(Sprite):
  def __init__(self, config):
    super().__init__()
    self.grid = [' ']*9

  def place(self, pos, let):
    self.grid[pos] = let
    
  def check(self):
    pass
  
  def update(self):
    pass
