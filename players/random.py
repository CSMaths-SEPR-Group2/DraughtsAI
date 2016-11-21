from Player import Player
import random
from game_parts import Board, Piece, Square, PieceType

class RandomPlayer(Player):
    def __init__(self, board: Board, color: PieceType):
        self._board = board
        self._color = color

    def make_move(self):
        all_moves = self._board.get_moves_by_colour(self._color)

        if not all_moves:
            print(self._board.get_str_form())
            raise Exception("No possible moves to make!")

        return random.choice(all_moves)

    def set_player_won(self):
        print(self._color.__repr__() + "wins!")
