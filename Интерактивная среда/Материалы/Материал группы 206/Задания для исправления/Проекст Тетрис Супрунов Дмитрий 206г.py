import pygame
import random
import os

WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
FPS = 10

COLORS = [
    (0, 0, 0), (255, 0, 0), (0, 255, 0),
    (0, 0, 255), (255, 255, 0), (255, 165, 0),
    (128, 0, 128), (0, 255, 255)
]

SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]  # Z
]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()


def draw_board(board):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x]:
                pygame.draw.rect(screen, COLORS[board[y][x]],
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE - 1, BLOCK_SIZE - 1))


def create_new_piece():
    shape = random.choice(SHAPES)
    color = COLORS[SHAPES.index(shape) + 1]
    return shape, color


def save_high_score(score):
    with open('high_scores.txt', 'a') as f:
        f.write(f"{score}\n")


def load_high_scores():
    if os.path.exists('high_scores.txt'):
        with open('high_scores.txt', 'r') as f:
            return [int(line.strip()) for line in f.readlines()]
    return []


def main():
    board = [[0] * (WIDTH // BLOCK_SIZE) for _ in range(HEIGHT // BLOCK_SIZE)]
    score = 0
    level = 1
    speed = FPS

    current_piece, current_color = create_new_piece()
    piece_x = WIDTH // BLOCK_SIZE // 2 - len(current_piece[0]) // 2
    piece_y = 0

    running = True
    while running:
        screen.fill((255, 255, 255))
        draw_board(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_high_score(score)
                running = False

        piece_y += 1

        if piece_y + len(current_piece) > len(board) or any(
                board[piece_y + y][piece_x + x] for y in range(len(current_piece)) for x in range(len(current_piece[y]))
                if current_piece[y][x]):
            piece_y -= 1
            for y in range(len(current_piece)):
                for x in range(len(current_piece[y])):
                    if current_piece[y][x]:
                        board[piece_y + y][piece_x + x] = SHAPES.index(current_piece) + 1

            for y in range(len(board) - 1, -1, -1):
                if all(board[y]):
                    del board[y]
                    board.insert(0, [0] * (WIDTH // BLOCK_SIZE))
                    score += 10

            current_piece, current_color = create_new_piece()
            piece_x = WIDTH // BLOCK_SIZE // 2 - len(current_piece[0]) // 2
            piece_y = 0

        for y in range(len(current_piece)):
            for x in range(len(current_piece[y])):
                if current_piece[y][x]:
                    pygame.draw.rect(screen, current_color,
                                     ((piece_x + x) * BLOCK_SIZE,
                                      (piece_y + y) * BLOCK_SIZE,
                                      BLOCK_SIZE - 1,
                                      BLOCK_SIZE - 1))

                    pygame.display.flip()
                    clock.tick(speed)

                    if score >= level * 100:
                        level += 1
                        speed += 2

                pygame.quit()

                if __name__ == "__main__":
                    main()