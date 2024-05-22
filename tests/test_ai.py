import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from game_pack.boards import Board
from game_pack.ai import Ai
from game_pack.params import WHITE, BLACK

def test_ai_initialization():
    board = Board(WHITE)
    ai = Ai(BLACK, board)
    assert ai.side == BLACK
    assert ai.board == board

def test_ai_get_next_move():
    board = Board(WHITE)
    ai = Ai(BLACK, board)
    move = ai.get_next_move()
    assert move is not None
