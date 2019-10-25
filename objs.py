from fxns import *


#contains settings for a game
class Config:
  def __init__(self):
    self.alt_settings = False
    self.screen_size = (600, 600)
    self.board_size = (500, 500)
    self.let_size = (40, 40)
    self.bg_color = (0, 0, 0)
    self.o_color = (128, 159, 255)
    self.x_color = (255, 0, 0)
    self.o_color_alt = (255, 255, 0)
    self.x_color_alt = (102, 0, 102)
    self.text_color = (255, 255, 255)


#contains all stats used by game objs
class Stats:
  def __init__(self):
    self.active = True
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
    self.image = image_scaler('t3_grid.png', config.board_size)
    self.rect = self.image.get_rect()
    self.rect.center = self.screen_rect.center
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

