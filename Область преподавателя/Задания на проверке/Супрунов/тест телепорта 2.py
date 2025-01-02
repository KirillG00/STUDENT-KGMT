import pygame
import random
import threading

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 1000, 1000
CELL_SIZE = 20
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE
FPS = 30

# Цвета
WHITE = (255, 255, 255)
DARK_GREEN = (0, 100, 0)
PLAYER_COLOR = (0, 0, 255)  # Цвет игрока
RABBIT_COLOR = (255, 0, 0)  # Цвет зайца
TELEPORT_COLOR = (0, 255, 0)  # Цвет телепорта

# Игровые переменные
player_pos = [COLS // 2, ROWS // 2]
rabbit_pos = [random.randint(1, COLS - 2), random.randint(1, ROWS - 2)]
maze = [[1 for _ in range(COLS)] for _ in range(ROWS)]
teleport_squares = [(random.randint(1, COLS - 2), random.randint(1, ROWS - 2)) for _ in range(3)]


def generate_maze():
    global maze, player_pos, rabbit_pos
    maze = [[1 for _ in range(COLS)] for _ in range(ROWS)]

    # Генерация лабиринта с одним проходом и без тупиков
    for r in range(1, ROWS - 1, 2):
        for c in range(1, COLS - 1, 2):
            maze[r][c] = 0
            if random.choice([True, False]) and r + 1 < ROWS - 1:
                maze[r + 1][c] = 0
            if c + 1 < COLS - 1:
                maze[r][c + 1] = 0

    # Убедимся, что игрок и заяц не появляются в тупиках
    while maze[player_pos[1]][player_pos[0]] == 1:
        player_pos[0], player_pos[1] = random.randint(1, COLS - 2), random.randint(1, ROWS - 2)

    while maze[rabbit_pos[1]][rabbit_pos[0]] == 1 or (rabbit_pos[0], rabbit_pos[1]) == (player_pos[0], player_pos[1]):
        rabbit_pos[0], rabbit_pos[1] = random.randint(1, COLS - 2), random.randint(1, ROWS - 2)


def draw_maze(screen):
    for r in range(ROWS):
        for c in range(COLS):
            if maze[r][c] == 1:
                pygame.draw.rect(screen, DARK_GREEN, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_player(screen):
    pygame.draw.rect(screen, PLAYER_COLOR, (player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_rabbit(screen):
    pygame.draw.rect(screen, RABBIT_COLOR, (rabbit_pos[0] * CELL_SIZE, rabbit_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_teleport_squares(screen):
    for index, (x, y) in enumerate(teleport_squares):
        pygame.draw.rect(screen, TELEPORT_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        # Отображение номера квадрата
        font = pygame.font.Font(None, 36)
        text_surface = font.render(str(index + 1), True, WHITE)
        screen.blit(text_surface, (x * CELL_SIZE + CELL_SIZE // 4, y * CELL_SIZE + CELL_SIZE // 4))


def is_valid_move(x, y):
    return 0 <= x < COLS and 0 <= y < ROWS and maze[y][x] == 0


def teleport_player(square_number):
    global player_pos
    if square_number > 0 and square_number <= len(teleport_squares):
        player_pos[:] = teleport_squares[square_number - 1]


def command_input():
    while True:
        command = input("Введите 't x' для телепортации или 'add' для добавления телепорта: ")
        parts = command.split()
        if len(parts) == 2 and parts[0] == 't':
            try:
                square_number = int(parts[1])
                teleport_player(square_number)
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите номер квадрата.")
        elif len(parts) == 1 and parts[0] == 'add':
            teleport_squares.append((player_pos[0], player_pos[1]))
            print(f"Телепорт добавлен в ({player_pos[0]}, {player_pos[1]})")


# Основной цикл игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Погоня за Зайцем")
clock = pygame.time.Clock()
running = True

# Запуск потока для ввода команд
threading.Thread(target=command_input, daemon=True).start()

generate_maze()

while running:
    screen.fill(WHITE)
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and is_valid_move(player_pos[0], player_pos[1] - 1):
        player_pos[1] -= 1
    if keys[pygame.K_DOWN] and is_valid_move(player_pos[0], player_pos[1] + 1):
        player_pos[1] += 1
    if keys[pygame.K_LEFT] and is_valid_move(player_pos[0] - 1, player_pos[1]):
        player_pos[0] -= 1
    if keys[pygame.K_RIGHT] and is_valid_move(player_pos[0] + 1, player_pos[1]):
        player_pos[0] += 1

    # Проверка на телепортацию при входе в квадрат
    for index, (x, y) in enumerate(teleport_squares):
        if player_pos == [x, y]:
            teleport_player(random.randint(1, len(teleport_squares)))

    # Отрисовка элементов на экране
    draw_maze(screen)
    draw_player(screen)
    draw_rabbit(screen)
    draw_teleport_squares(screen)

    # Отображение координат игрока
    font = pygame.font.Font(None, 36)
    coord_text = f"X: {player_pos[0]}, Y: {player_pos[1]}"
    text_surface = font.render(coord_text, True, (0, 0, 0))
    screen.blit(text_surface, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

# Завершение работы Pygame
pygame.quit()
