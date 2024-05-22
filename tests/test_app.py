import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app, socketio
from flask import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def socketio_client():
    client = socketio.test_client(app)
    yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_start_game(socketio_client):
    socketio_client.emit('start_game', {'side': 'white'})
    received = socketio_client.get_received()
    assert len(received) > 0

def test_make_move(socketio_client):
    socketio_client.emit('start_game', {'side': 'white'})
    socketio_client.emit('make_move', {'new_row': 2, 'new_col': 0})
    received = socketio_client.get_received()
    assert len(received) > 0
