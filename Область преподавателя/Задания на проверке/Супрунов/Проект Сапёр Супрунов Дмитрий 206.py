import pygame
import random
import json
import os

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)
BLACK = (0, 0, 0)

# Размеры экрана и поля
WIDTH = 400
HEIGHT = 400
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Minesweeper')

# Путь к файлу для сохранения данных
data_file = 'scores.json'


def load_scores():
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    return {}


def save_scores(scores):
    with open(data_file, 'w') as f:
        json.dump(scores, f)


def get_name():
    name = ""
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                input_active = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

        screen.fill(BLUE)
        font = pygame.font.SysFont("bahnschrift", 25)
        text_surface = font.render("Enter your name: " + name, True, WHITE)
        screen.blit(text_surface, [WIDTH / 6, HEIGHT / 3])
        pygame.display.update()

    return name


class Cell:
    def __init__(self):
        self.is_mine = False
        self.is_revealed = False
        self.neighbor_mines = 0

    def reveal(self):
        self.is_revealed = True


class Minesweeper:
    def __init__(self):
        self.grid = [[Cell() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.game_over = False
        self.mines_count = 10
        self.score = 0

        # Расставляем мины
        self.place_mines()
        self.calculate_neighbors()

    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.mines_count:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            if not self.grid[x][y].is_mine:
                self.grid[x][y].is_mine = True
                mines_placed += 1

    def calculate_neighbors(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                if self.grid[x][y].is_mine:
                    continue
                count = sum(
                    1 for dx in (-1, 0, 1) for dy in (-1, 0, 1)
                    if 0 <= x + dx < GRID_SIZE and 0 <= y + dy < GRID_SIZE and self.grid[x + dx][y + dy].is_mine
                )
                self.grid[x][y].neighbor_mines = count

    def reveal_cell(self, x, y):
        if self.grid[x][y].is_revealed or self.game_over:
            return

        self.grid[x][y].reveal()
        if self.grid[x][y].is_mine:
            self.game_over = True
            return

        self.score += 1

        if self.grid[x][y].neighbor_mines == 0:
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                        self.reveal_cell(nx, ny)

    def draw(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                cell = self.grid[x][y]
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

                if cell.is_revealed:
                    if cell.is_mine:
                        color = RED
                    else:
                        color = GREEN if cell.neighbor_mines == 0 else YELLOW
                else:
                    color = BLACK

                pygame.draw.rect(screen, color, rect)
                pygame.draw.rect(screen, WHITE, rect, 1)

                if cell.is_revealed and cell.neighbor_mines > 0:
                    font = pygame.font.SysFont("bahnschrift", 20)
                    text_surface = font.render(str(cell.neighbor_mines), True, WHITE)
                    screen.blit(text_surface, (x * CELL_SIZE + CELL_SIZE // 3, y * CELL_SIZE + CELL_SIZE // 4))

    def reset(self):
        self.__init__()


def main_menu():
    while True:
        screen.fill(BLUE)
        font = pygame.font.SysFont("bahnschrift", 25)
        title_surface = font.render("Welcome to Minesweeper!", True, WHITE)
        instruction_surface = font.render("Press ENTER to start or ESC to exit", True, WHITE)

        screen.blit(title_surface, [WIDTH / 6, HEIGHT / 3])
        screen.blit(instruction_surface, [WIDTH / 6, HEIGHT / 2])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player_name = get_name()
                    game_loop(player_name)
                elif event.key == pygame.K_ESCAPE:
                    return False


def game_loop(name):
    game = Minesweeper()
    clock = pygame.time.Clock()

    while True:
        screen.fill(BLUE)
        
        game.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                x = mouse_x // CELL_SIZE
                y = mouse_y // CELL_SIZE
                
                game.reveal_cell(x, y)

                if game.game_over:
                    scores = load_scores()
                    scores[name] = max(scores.get(name, 0), game.score)
                    save_scores(scores)

                    # Перезапуск игры после окончания
                    game.reset()
        
        # Отображение счета
        font = pygame.font.SysFont("bahnschrift", 25)
        score_surface = font.render(f"Score: {game.score}", True, WHITE)
        screen.blit(score_surface, [10, 10])

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    main_menu()
    pygame.quit()
