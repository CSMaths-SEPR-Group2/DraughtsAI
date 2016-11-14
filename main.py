from game_parts import *
from players.random import RandomPlayer

board = Board()
board.init_default_state()

player1 = RandomPlayer(board, PieceType.White)
player2 = RandomPlayer(board, PieceType.Black)

winner = None

while True:
    player1_move = player1.make_move()
    print(player1_move)
    board.apply_move(player1_move)
    if board.has_player_lost(PieceType.Black):
        winner = PieceType.White
        break

    player2_move = player2.make_move()
    board.apply_move(player2_move)
    if board.has_player_lost(PieceType.White):
        winner = PieceType.Black
        break