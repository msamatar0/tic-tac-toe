import pygame, sys, time
from pygame import *

class Board:
  def __init__(self):
    self.grid = [' ']*9

  def place(self, pos, let):
    self.grid[pos] = let

  def check(self):
    pass
