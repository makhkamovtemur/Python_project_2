from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
from game_pack.boards import Board
from game_pack.params import WHITE, BLACK, CELL_SIZE, OPPOSITE_SIDE
from game_pack.ai import Ai

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Глобальные переменные для игрового состояния
board = None
ai = None
player_side = None
computer_side = None
selected_figure = None
avl_moves = []
selected_move = None
shah_flag = False
msg = None

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('start_game')
def handle_start_game(data):
    global board, ai, player_side, computer_side
    player_side = WHITE if data['side'] == 'white' else BLACK
    computer_side = OPPOSITE_SIDE[player_side]
    board = Board(player_side)
    ai = Ai(computer_side, board)
    check_position = get_check_position()
    if computer_side == WHITE:
        handle_computer_move()
    emit('game_started', {'player_side': player_side, 'board': get_board_state(), 'check_position': check_position})

@socketio.on('get_moves')
def handle_get_moves(data):
    global avl_moves
    row, col = data['row'], data['col']
    selected_figure = board.get_figure(row, col)
    if selected_figure and selected_figure.side == player_side:
        avl_moves = board.get_avl_moves_for_figure(selected_figure)
        moves = [{'new_row': move.new_row, 'new_col': move.new_col} for move in avl_moves]
        emit('available_moves', {'moves': moves})

def get_board_state():
    board_state = []
    for row in range(8):
        board_row = []
        for col in range(8):
            figure = board.get_figure(row, col)
            if figure is not None:
                board_row.append((figure.side, type(figure).__name__))
            else:
                board_row.append(None)
        board_state.append(board_row)
    return board_state

@socketio.on('make_move')
def handle_make_move(data):
    global selected_move, selected_figure, avl_moves, shah_flag, msg
    # Обработка хода игрока
    selected_move = None
    for move in avl_moves:
        if move.new_row == data['new_row'] and move.new_col == data['new_col']:
            selected_move = move
            break
    if selected_move:
        board.apply_move(selected_move)
        selected_figure = None
        avl_moves = []
        shah_flag = False
        game_over = check_game_over(computer_side)
        check_position = get_check_position()
        if game_over:
            msg = 'You win!' if game_over == 'mat' else 'Draw'
            emit('game_over', {'msg': msg})
            return
        emit('move_made', {'board': get_board_state(), 'check_position': check_position})
        handle_computer_move()

def handle_computer_move():
    global selected_move, shah_flag, msg
    move = ai.get_next_move()
    board.apply_move(move)
    shah_flag = board.is_strike_figure(board.pl_king)
    game_over = check_game_over(player_side)
    check_position = get_check_position()
    if game_over:
        msg = 'You lose!' if game_over == 'mat' else 'Draw'
        emit('game_over', {'msg': msg})
        return
    emit('move_made', {'board': get_board_state(), 'check_position': check_position})


def get_check_position():
    for side in [WHITE, BLACK]:
        king = board.kings_dict[side]
        if board.is_strike_figure(king):
            return {'row': king.row, 'col': king.col}
    return None

def check_game_over(side):
    king = board.kings_dict[side]
    sh_flag = board.is_strike_figure(king)
    avl_flag = (len(board.get_all_avl_moves(side)) == 0)
    if avl_flag and sh_flag:
        return 'mat'
    if avl_flag and not sh_flag:
        return 'pat'
    return None

if __name__ == '__main__':
    socketio.run(app, debug=True)
