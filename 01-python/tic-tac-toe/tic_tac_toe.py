import re
import random

_PLAYER = "player"
_MACHINE = "machine"
_DRAW = "draw"

_PLAYER_SYMBOL = "x"
_MACHINE_SYMBOL = "o"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self): # TODO: Finish this function by adding checks for a winning game (rows, columns, diagonals)
    #diagonals
    if self.board[4] is not None: #center not Null
      if self.board[4] is _MACHINE_SYMBOL:
        if ((self.board[0] == _MACHINE_SYMBOL and self.board[8] == _MACHINE_SYMBOL) or (self.board[2] == _MACHINE_SYMBOL and self.board[6] == _MACHINE_SYMBOL)):
          self.winner = _MACHINE #diagonals
          return True
        if ((self.board[1] == _MACHINE_SYMBOL and self.board[7] == _MACHINE_SYMBOL) or (self.board[3] == _MACHINE_SYMBOL and self.board[5] == _MACHINE_SYMBOL)):
          self.winner = _MACHINE #cross
          return True
      elif ((self.board[0] == _PLAYER_SYMBOL and self.board[8] == _PLAYER_SYMBOL) or (self.board[2] == _PLAYER_SYMBOL and self.board[6] == _PLAYER_SYMBOL)):
        self.winner = _PLAYER #diagonals
        return True
      elif ((self.board[1] == _PLAYER_SYMBOL and self.board[7] == _PLAYER_SYMBOL) or (self.board[3] == _PLAYER_SYMBOL and self.board[5] == _PLAYER_SYMBOL)):
        self.winner = _PLAYER #cross
        return True
    # 0 cell corner (first row or first column)
    elif (self.board[0] is not None):
      if self.board[0] is _MACHINE_SYMBOL:
        if ((self.board[1] == _MACHINE_SYMBOL and self.board[2] == _MACHINE_SYMBOL) or (self.board[3] == _MACHINE_SYMBOL and self.board[6] == _MACHINE_SYMBOL)):
          self.winner = _MACHINE
          return True
      elif self.board[0] is _PLAYER_SYMBOL:
        if ((self.board[1] == _PLAYER_SYMBOL and self.board[2] == _PLAYER_SYMBOL) or (self.board[3] == _PLAYER_SYMBOL and self.board[6] == _PLAYER_SYMBOL)):
          self.winner = _PLAYER
          return True
    # 8 cell corner (last row or last column)
    elif (self.board[8] is not None):
      if self.board[8] is _MACHINE_SYMBOL:
        if ((self.board[6] == _MACHINE_SYMBOL and self.board[7] == _MACHINE_SYMBOL) or (self.board[2] == _MACHINE_SYMBOL and self.board[5] == _MACHINE_SYMBOL)):
          self.winner = _MACHINE
          return True
      elif self.board[8] is _PLAYER_SYMBOL:
        if ((self.board[6] == _PLAYER_SYMBOL and self.board[7] == _PLAYER_SYMBOL) or (self.board[2] == _PLAYER_SYMBOL and self.board[5] == _PLAYER_SYMBOL)):
          self.winner = _PLAYER
          return True
    # no one has won
    if (self.board.count(None) == 0): # and there are no more blank spaces
      self.winner = _DRAW #game over. draw
      return True
    # there are still blank spaces
    return False

  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER
    self.is_over()

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self): # TODO: Finish this function by making the machine choose a random cell (use random module)
    out = False
    while (not out):
      randomN = random.randint(0,8)
      cell = self.board[randomN]
      if cell is None:
        self.board[randomN] = _MACHINE_SYMBOL
        out = True

  def format_board(self):
    row0 = "|".join(list(map(lambda c: " " if c is None else c, self.board[0:3])))
    row1 = "|".join(list(map(lambda c: " " if c is None else c, self.board[3:6])))
    row2 = "|".join(list(map(lambda c: " " if c is None else c, self.board[6:9])))

    return "\n".join([row0, row1, row2])

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self): # TODO: Finish this function in order to print the result based on the *winner*
    if (self.winner == _DRAW):
      print("Game Over. "+_DRAW)
    else:
      print("Game Over. Winner: "+self.winner)
