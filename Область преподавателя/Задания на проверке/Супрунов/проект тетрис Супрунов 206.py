import pygame
import random
import os

pygame.time.delay(2000)
WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
ROWS, COLS = HEIGHT // BLOCK_SIZE, WIDTH // BLOCK_SIZE

COLORS = [
    (0, 255, 255),
    (255, 165, 0),
    (0, 0, 255),
    (255, 0, 0),
    (0, 255, 0),
    (128, 0, 128),
    (255, 255, 0)
]

SHAPES = [
    [[1, 1], [1, 1]],
    [[0, 1, 0], [1, 1, 1]],
    [[0, 1], [0, 1], [1, 1]],
    [[1, 0], [1, 0], [1, 1]],
    [[1, 1], [0, 1], [0, 1]],
    [[1, 1], [1, 1]],
    [[1], [1], [1], [1]]
]

class Tetris:
    def __init__(self):
        self.board = [[0] * COLS for _ in range(ROWS)]
        self.score = 0
        self.high_score = self.load_high_score()
        self.current_shape = self.get_new_shape()
        self.next_shape = self.get_new_shape()
        self.current_x = COLS // 2 - len(self.current_shape[0]) // 2
        self.current_y = 0
        self.fall_time = 0
        self.fall_speed = 500

    def load_high_score(self):
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as f:
                return int(f.read())
        return 0

    def save_high_score(self):
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))

    def get_new_shape(self):
        shape = random.choice(SHAPES)
        color = random.choice(COLORS)
        return shape, color

    def rotate_shape(self):
        self.current_shape[0] = [list(row) for row in zip(*self.current_shape[0][::-1])]

    def draw_board(self, surface):
        for r in range(ROWS):
            for c in range(COLS):
                if self.board[r][c]:
                    pygame.draw.rect(surface, self.board[r][c],
                                     (c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1))

    def draw_shape(self, surface):
        shape, color = self.current_shape
        for r in range(len(shape)):
            for c in range(len(shape[r])):
                if shape[r][c]:
                    pygame.draw.rect(surface, color,
                                     ((self.current_x + c) * BLOCK_SIZE,
                                      (self.current_y + r) * BLOCK_SIZE,
                                      BLOCK_SIZE - 1, BLOCK_SIZE - 1))

    def drop(self):
        self.current_y += 1
        if self.check_collision():
            self.current_y -= 1
            self.lock_shape()
            self.clear_lines()
            self.current_shape = self.next_shape
            self.next_shape = self.get_new_shape()
            if self.check_collision():
                print("Game Over")
                self.reset_game()

    def check_collision(self):
        shape, _ = self.current_shape
        for r in range(len(shape)):
            for c in range(len(shape[r])):
                if shape[r][c]:
                    x = self.current_x + c
                    y = self.current_y + r
                    if x < 0 or x >= COLS or y >= ROWS or (y >= 0 and self.board[y][x]):
                        return True
        return False
def lock_shape(self):
    for r in range(len(self.shape)):
        for c in range(len(self.shape[r])):
            if self.shape[r][c]:  # Проверяем, что это часть фигуры
                new_y = self.current_y + r
                new_x = self.current_x + c
                
                if 0 <= new_y < len(self.board) and 0 <= new_x < len(self.board[0]):
                    self.board[new_y][new_x] = COLORS
                else:
                    print(f"Индекс вне границ: y={new_y}, x={new_x}")

    def lock_shape(self):
        shape, color = self.current_shape
        for r in range(len(shape)):
            for c in range(len(shape[r])):
                if shape[r][c]:
                    self.board[self.current_y + r][self.current_x + c] = color

    def clear_lines(self):
        lines_to_clear = []
        for r in range(ROWS):
            if all(self.board[r]):
                lines_to_clear.append(r)

        for r in lines_to_clear:
            del self.board[r]
            self.board.insert(0, [0] * COLS)
            self.score += len(lines_to_clear) * 100

        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def reset_game(self):
        self.board = [[0] * COLS for _ in range(ROWS)]
        self.score = 0
        self.current_shape = self.get_new_shape()
        self.next_shape = self.get_new_shape()

pygame.init()
screen = pygame.display.set_mode((WIDTH + 200, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
game = Tetris()

def draw_menu(surface):
    font = pygame.font.Font(None, 48)
    title_text = font.render('Tetris', True, (255, 255, 255))
    start_text = font.render('Press Enter to Start', True, (255, 255, 255))
    
    surface.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 2 - title_text.get_height() // 2 - 20))
    surface.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 + start_text.get_height() // 2))

def draw_pause(surface):
    font = pygame.font.Font(None, 48)
    pause_text = font.render('Paused', True, (255, 255, 255))
    
    surface.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2 - pause_text.get_height() // 2))

running = True
paused = False

while running:
    screen.fill((0, 0, 0))

    if not paused:
        game.draw_board(screen)
        game.draw_shape(screen)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {game.score}', True, (255, 255, 255))
        high_score_text = font.render(f'High Score: {game.high_score}', True, (255, 255, 255))
        
        screen.blit(score_text, (WIDTH + 10, 10))
        screen.blit(high_score_text, (WIDTH + 10, 50))

        next_shape_surface = pygame.Surface((100, 100))
        next_shape_surface.fill((0, 0, 0))
        
        next_shape_color = game.next_shape[1]
        
        for r in range(len(game.next_shape[0])):
            for c in range(len(game.next_shape[0][r])):
                if game.next_shape[0][r][c]:
                    pygame.draw.rect(next_shape_surface,
                                     next_shape_color,
                                     (c * BLOCK_SIZE // 3 + WIDTH +10,
                                      r * BLOCK_SIZE // 3 + HEIGHT //2,
                                      BLOCK_SIZE //3 -1 , BLOCK_SIZE //3 -1))

        screen.blit(next_shape_surface,(WIDTH +10 , HEIGHT //2))

        game.fall_time += clock.get_time()
        
        if game.fall_time >= game.fall_speed:
            game.drop()
            game.fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.current_x -= 1
                    if game.check_collision():
                        game.current_x += 1
                
                if event.key == pygame.K_RIGHT:
                    game.current_x += 1
                    if game.check_collision():
                        game.current_x -= 1
                
                if event.key == pygame.K_DOWN:
                    game.drop()
                
                if event.key == pygame.K_UP:
                    game.rotate_shape()
                    if game.check_collision():
                        game.rotate_shape()

                if event.key == pygame.K_SPACE:
                    game.fall_speed = max(100, game.fall_speed // 2)
                if event.key == pygame.K_p:
                    paused = True

                if event.key == pygame.K_RETURN:
                    game.reset_game()

            if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                game.fall_speed *= 2

    else: 
        draw_pause(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
