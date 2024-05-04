# Chess Web App
Версия: 1.0
Автор: Махкамов Темур (makhkamovtemur@gmail.com)

## Описание
Chess веб-приложение для игры в шахматы, позволяющее пользователям играть друг с другом в реальном времени.

## Основные функции
1. **Поиск и выбор оппонента:** Пользователи могут искать доступных оппонентов онлайн и начинать игру.
2. **Многопользовательская игра:** Поддержка нескольких игровых сессий одновременно.
3. **Символьная и рисованная графика:** Игровое поле отображается с использованием как символьной, так и графической визуализации.
4. **Таблица результатов:** Отображение текущих и прошлых результатов игр.
5. **Режим игры с компьютером:** Возможность играть против искусственного интеллекта.
6. **Поддержка рейтинга игроков:** Игроки могут набирать рейтинг, который сохраняется и отображается в профиле.
7. **Запоминание результатов игр между запусками:** Работа с базой данных для сохранения истории игр и статистики пользователей.

## Технологии и библиотеки
* Python 3.8
* Flask (для создания веб-сервера)
* SQLAlchemy (для работы с базой данных)
* HTML/CSS (для визуализации интерфейса)

## Структура проекта
* `app.py` - основной файл сервера.
* `static/` - папка с статическими файлами (CSS, JS, изображения).
* `templates/` - папка с HTML шаблонами.
* `models.py` - модели базы данных.
* `chess_logic.py` - модуль с логикой игры в шахматы.

## Классы и модули

### ChessGame
Основной класс для логики шахматной игры:
- `start_game()`: Запускает новую игру между двумя игроками.
- `make_move(player, move)`: Обрабатывает ход игрока.
- `check_status()`: Проверяет состояние игры (шах, мат, пат).

### Player
Класс для игрока:
- `make_move(move)`: Отправляет ход на сервер.
- `update_stats(result)`: Обновляет статистику игрока после игры.

### GameSession
Класс для отдельной сессии игры:
- `save_session()`: Сохраняет текущее состояние игры в базу данных.
- `load_session(session_id)`: Загружает сохраненную игровую сессию.
