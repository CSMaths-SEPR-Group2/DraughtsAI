from Player import Player
import random
from game_parts import Board, Piece, Square, PieceType

class RandomPlayer(Player):
    def __init__(self, board: Board, color: PieceType):
        self._board = board
        self._color = color

    def make_move(self):
        allmoves = self._board.get_moves_by_colour(self._color)
        return random.choice(allmoves)

