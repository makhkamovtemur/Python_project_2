import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from game_pack.boards import Board
from game_pack.figures import Figure
from game_pack.params import WHITE

def test_figure_initialization():
    board = Board(WHITE)
    figure = Figure('whitePawn.png', 1, 0, WHITE, board)
    assert figure.row == 1
    assert figure.col == 0
    assert figure.side == WHITE

def test_set_pos():
    board = Board(WHITE)
    figure = Figure('whitePawn.png', 1, 0, WHITE, board)
    figure.set_pos(2, 0)
    assert figure.row == 2
    assert figure.col == 0

def test_get_actions():
    board = Board(WHITE)
    figure = board.get_figure(1, 0)
    actions = figure.get_actions()
    assert len(actions) > 0
