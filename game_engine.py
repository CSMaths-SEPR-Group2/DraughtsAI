from Player import Player
from game_parts import *
from typing import Type
from players.random import RandomPlayer


def start_game(Player1Type: Type[Player], Player2Type: Type[Player]):
    board = Board()
    board.init_default_state()

    player1 = Player1Type(board, PieceType.White)
    player2 = Player2Type(board, PieceType.Black)

    while True:
        player1_move = player1.make_move()
        print(player1_move)
        board.apply_move(player1_move)
        if board.has_player_lost(PieceType.Black):
            player1.set_player_won()

            break

        player2_move = player2.make_move()
        board.apply_move(player2_move)
        if board.has_player_lost(PieceType.White):
            player2.set_player_won()
            break