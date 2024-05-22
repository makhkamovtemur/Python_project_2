import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from game_pack.boards import Board
from game_pack.params import WHITE, BLACK

def test_board_initialization():
    board = Board(WHITE)
    assert board.pl_side == WHITE

def test_get_figure():
    board = Board(WHITE)
    figure = board.get_figure(0, 0)
    assert figure is not None

def test_apply_move():
    board = Board(WHITE)
    move = board.get_all_avl_moves(WHITE)[0]
    board.apply_move(move)
    assert board.get_figure(move.new_row, move.new_col) is not None
