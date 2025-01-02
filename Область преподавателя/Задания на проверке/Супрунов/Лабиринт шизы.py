import pygame
import random
import time

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

# Игровые переменные
player_pos = [COLS // 2, ROWS // 2]
rabbit_pos = [COLS // 2, ROWS // 2]
rabbit_color = (255, 0, 0)
maze = [[1 for _ in range(COLS)] for _ in range(ROWS)]
can_break_wall = True
break_cooldown = 60
last_break_time = time.time()


def generate_maze():
    global maze, player_pos, rabbit_pos
    maze = [[1 for _ in range(COLS)] for _ in range(ROWS)]

    # Генерация лабиринта с одним проходом
    for r in range(1, ROWS - 1, 2):
        for c in range(1, COLS - 1, 2):
            maze[r][c] = 0
            if random.choice([True, False]) and r + 1 < ROWS - 1:
                maze[r + 1][c] = 0
            if c + 1 < COLS - 1:
                maze[r][c + 1] = 0

    # Убедимся, что игрок и заяц не появляются в тупиках
    while maze[player_pos[1]][player_pos[0]] == 1:
        player_pos[0], player_pos[1] = COLS // 2, ROWS // 2

    while maze[rabbit_pos[1]][rabbit_pos[0]] == 1 or (rabbit_pos[0], rabbit_pos[1]) == (player_pos[0], player_pos[1]):
        rabbit_pos[0], rabbit_pos[1] = random.randint(1, COLS - 2), random.randint(1, ROWS - 2)


def draw_maze(screen):
    for r in range(ROWS):
        for c in range(COLS):
            if maze[r][c] == 1:
                pygame.draw.rect(screen, DARK_GREEN, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_player(screen):
    pygame.draw.rect(screen, (0, 0, 0), (player_pos[0] * CELL_SIZE, player_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_rabbit(screen):
    pygame.draw.rect(screen, rabbit_color, (rabbit_pos[0] * CELL_SIZE, rabbit_pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def is_valid_move(x, y):
    return 0 <= x < COLS and 0 <= y < ROWS and maze[y][x] == 0


def reset_game():
    global player_pos, rabbit_pos
    player_pos[0], player_pos[1] = COLS // 2, ROWS // 2
    rabbit_pos[0], rabbit_pos[1] = random.randint(1, COLS - 2), random.randint(1, ROWS - 2)
    generate_maze()


def move_rabbit():
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # вверх, вниз, влево, вправо
    best_direction = None
    max_distance = -1

    for dx, dy in directions:
        new_x = rabbit_pos[0] + dx
        new_y = rabbit_pos[1] + dy
        if is_valid_move(new_x, new_y):
            distance = ((new_x - player_pos[0]) ** 2 + (new_y - player_pos[1]) ** 2) ** 0.5
            if distance > max_distance:
                max_distance = distance
                best_direction = (dx, dy)

    if best_direction:
        rabbit_pos[0] += best_direction[0]
        rabbit_pos[1] += best_direction[1]


def break_wall(x, y):
    if is_valid_move(x, y) and can_break_wall:
        maze[y][x] = 0


# Основной цикл игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Погоня за Зайцем")
clock = pygame.time.Clock()
running = True

generate_maze()
start_time = time.time()

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

    # Ломаем стену при нажатии мыши
    if pygame.mouse.get_pressed()[0]: # Левая кнопка мыши
        current_time = time.time()
        if current_time - last_break_time >= break_cooldown:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            block_x = mouse_x // CELL_SIZE
            block_y = mouse_y // CELL_SIZE
            break_wall(block_x, block_y)
            last_break_time = current_time

    # Двигаем зайца
    move_rabbit()

    # Проверка на ловлю зайца
    if player_pos == rabbit_pos:
        print("Вы поймали зайца!")
        reset_game()

    # Рисуем лабиринт и игрока
    draw_maze(screen)
    draw_player(screen)
    draw_rabbit(screen)

    # Меняем цвет зайца и лабиринт каждые 30 секунд
    if time.time() - start_time > 30:
        rabbit_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        generate_maze()
        start_time = time.time()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
