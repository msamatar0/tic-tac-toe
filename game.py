from objs import *

config = Config()
stats = Stats()

def run_game():
  pygame.init()
  screen = pygame.display.set_mode(config.screen_size)
  board = Board(config, screen, stats)

  while True:
    events(config, board)
    board.blitme()
    pygame.display.flip()

run_game()