# Chess Web App
Версия: 1.0
Автор: Махкамов Темур (makhkamovtemur@gmail.com)

## Описание
Шахматная программа написанная на Python 3.7 с использованием Flask и Pygame для создания веб-приложения. Программа позволяет пользователям играть в шахматы против компьютера, используя алгоритм минимакс для расчета ходов

## Технологии и библиотеки
* Python 3.8
* Pygame
* Flask (для создания веб-сервера)
* Flask-SocketIO (для работы с веб-сокетами)
* PyCharm или другую IDE, поддерживающую разработку на Python
* HTML/CSS (для визуализации интерфейса)

## Структура файлов
Project_2/
├── pythonProject2/
│   ├── game_pack/
│   │   ├── __init__.py
│   │   ├── ai.py
│   │   ├── boards.py
│   │   ├── figures.py
│   │   └── params.py
│   ├── static/
│   │   ├── sprites/
│   │   │   ├── blackBishop.png
│   │   │   ├── blackKing.png
│   │   │   ├── blackKnight.png
│   │   │   ├── blackPawn.png
│   │   │   ├── blackQueen.png
│   │   │   ├── blackRook.png
│   │   │   ├── whiteBishop.png
│   │   │   ├── whiteKing.png
│   │   │   ├── whiteKnight.png
│   │   │   ├── whitePawn.png
│   │   │   ├── whiteQueen.png
│   │   │   └── whiteRook.png
│   │   └── style.css
│   ├── templates/
│   │   └── index.html
│   └── app.py

## Структура проекта
* `app.py` - основной файл сервера.
* `static/` - папка с статическими файлами (CSS, JS, изображения).
* `templates/` - папка с HTML шаблонами.
	* `templates/sprites` - изображения фигур и доски
* `game_pack/` - модуль с логикой игры в шахматы.

## Реализуемый функционал
1. Веб-интерфейс для игры в шахматы
2. Подсчет доступных ходов
3. Подсветка шаха
4. Минимакс алгоритм

## Классы и модули

### `ai.py`
Алгоритм минимакс для расчета ходов компьютера.

**Атрибуты**:
- `side` (str): Сторона (белые или черные), за которую играет компьютер.
- `board` (Board): Текущее состояние игрового поля.

**Методы**:
- `get_next_move() -> Move`: Возвращает следующий ход, рассчитанный алгоритмом минимакс.

### `boards.py`
Управление игровым полем и ходами.

**Класс `Board`**:
- **Атрибуты**:
  - `player_side` (str): Сторона, за которую играет пользователь.
  - `kings_dict` (dict): Словарь с королями на доске.
- **Методы**:
  - `get_figure(row: int, col: int) -> Figure`: Возвращает фигуру, находящуюся на заданной клетке.
  - `apply_move(move: Move)`: Применяет заданный ход.
  - `get_all_avl_moves(side: str) -> list`: Возвращает все доступные ходы для заданной стороны.

### `figures.py`
Классы, описывающие шахматные фигуры.

**Класс `Figure`**:
- **Атрибуты**:
  - `image_path` (str): Путь к изображению фигуры.
  - `row` (int): Ряд, в котором находится фигура.
  - `col` (int): Колонка, в которой находится фигура.
  - `side` (str): Сторона (белые или черные), к которой принадлежит фигура.
- **Методы**:
  - `set_pos(r: int, c: int)`: Устанавливает новое положение фигуры.
  - `get_actions() -> list`: Возвращает список доступных ходов для фигуры.

### `params.py`
Параметры игры: цветовые константы, типы ходов, список приоритетов фигур и т.д.

## Пример использования
1. Запустите приложение:
    ```sh
    python app.py
    ```
2. Откройте браузер и перейдите по адресу [http://127.0.0.1:5000](http://127.0.0.1:5000).
3. Выберите сторону (белые или черные) и начните игру

## Тесты
Тесты можно найти в папке tests

---------- coverage: platform win32, python 3.12.3-final-0 -----------
Name                    Stmts   Miss  Cover
-------------------------------------------
app.py                     97     42    57%
game_pack\__init__.py       0      0   100%
game_pack\ai.py            59     44    25%
game_pack\boards.py       349    146    58%
game_pack\figures.py      130      0   100%
game_pack\params.py        23      0   100%
-------------------------------------------
TOTAL                     658    232    65%
