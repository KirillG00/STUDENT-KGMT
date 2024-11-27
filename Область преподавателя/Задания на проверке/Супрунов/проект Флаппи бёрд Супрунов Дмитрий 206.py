import pygame
import random
import json
import os

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Размеры экрана
WIDTH = 400
HEIGHT = 600

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

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

class Bird:
    def __init__(self):
        self.x = 50
        self.y = HEIGHT // 2
        self.gravity = 0.5
        self.velocity = 0
        self.jump_strength = -10
        self.image = pygame.Surface((30, 30))
        self.image.fill(GREEN)

    def jump(self):
        self.velocity = self.jump_strength

    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Pipe:
    def __init__(self):
        self.width = 70
        self.gap = 150
        self.x = WIDTH
        self.height = random.randint(100, HEIGHT - self.gap - 100)
        self.passed = False

    def update(self):
        self.x -= 5

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, 0, self.width, self.height))  # верхняя труба
        pygame.draw.rect(screen, GREEN, (self.x, self.height + self.gap, self.width, HEIGHT - self.height - self.gap))  # нижняя труба

def main_menu():
    while True:
        screen.fill(BLUE)
        font = pygame.font.SysFont("bahnschrift", 25)
        title_surface = font.render("Welcome to Flappy Bird!", True, WHITE)
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

def game_over_screen(score, high_score):
    while True:
        screen.fill(BLUE)
        font = pygame.font.SysFont("bahnschrift", 35)
        game_over_surface = font.render("Game Over!", True, WHITE)
        score_surface = font.render(f'Your Score: {score}', True, WHITE)
        high_score_surface = font.render(f'High Score: {high_score}', True, WHITE)
        instruction_surface = font.render("Press ENTER to restart or ESC to exit", True, WHITE)

        screen.blit(game_over_surface, [WIDTH / 4, HEIGHT / 3])
        screen.blit(score_surface, [WIDTH / 4, HEIGHT / 2])
        screen.blit(high_score_surface, [WIDTH / 4, HEIGHT / 2 + 40])
        screen.blit(instruction_surface, [WIDTH / 6, HEIGHT / 2 + 80])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False

def game_loop(name):
    bird = Bird()
    pipes = [Pipe()]
    clock = pygame.time.Clock()
    score = 0
    high_score_data = load_scores()
    high_score = high_score_data.get(name, 0)

    while True:
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()
                if event.key == pygame.K_ESCAPE:
                    return

        bird.update()

        if bird.y > HEIGHT or bird.y < 0:
            break

        if pipes[-1].x < WIDTH - 250:  # увеличиваем расстояние между трубами
            pipes.append(Pipe())

        for pipe in pipes:
            pipe.update()
            if pipe.x + pipe.width < bird.x and not pipe.passed:
                score += 1
                pipe.passed = True
            
            # Проверка на столкновение с трубами
            if pipe.x < bird.x < pipe.x + pipe.width:  
                if bird.y < pipe.height or bird.y + 30 > pipe.height + pipe.gap:
                    break
            
            if pipe.x < -pipe.width:  
                pipes.remove(pipe)

            pipe.draw()

        bird.draw()

        # Отображаем счет и рекорд
        font = pygame.font.SysFont("bahnschrift", 30)
        score_surface = font.render(f'Score: {score}', True, WHITE)
        high_score_surface = font.render(f'High Score: {high_score}', True, WHITE)
        
        screen.blit(score_surface, (10, 10))
        screen.blit(high_score_surface, (10, 40))

        # Сохраняем рекорд
        if score > high_score:
            high_score_data[name] = score
            save_scores(high_score_data)

        pygame.display.update()
        clock.tick(30)

    # Показать экран Game Over после завершения игры
    if not game_over_screen(score, high_score):
        return

if __name__ == "__main__":
    main_menu()
    pygame.quit()
