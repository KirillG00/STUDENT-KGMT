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
RED = (213, 50, 80)
BLUE = (50, 153, 213)

# Размеры экрана
WIDTH = 600
HEIGHT = 400

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Hangman Game')

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

class HangmanGame:
    def __init__(self):
        self.words = ['python', 'hangman', 'pygame', 'programming', 'challenge']
        self.word = random.choice(self.words).upper()
        self.guesses = []
        self.max_attempts = 6
        self.attempts_left = self.max_attempts
        self.score = 0
        self.game_over = False

    def guess(self, letter):
        if letter not in self.guesses:
            self.guesses.append(letter)
            if letter not in self.word:
                self.attempts_left -= 1

    def check_win(self):
        return all(letter in self.guesses for letter in self.word)

    def reset(self):
        self.__init__()

def draw_hangman(attempts):
    # Рисуем виселицу и тело в зависимости от количества оставшихся попыток
    if attempts < 6:
        pygame.draw.line(screen, BLACK, (150, 350), (300, 350), 5)  # основание
    if attempts < 5:
        pygame.draw.line(screen, BLACK, (200, 350), (200, 50), 5)   # столб
    if attempts < 4:
        pygame.draw.line(screen, BLACK, (200, 50), (300, 50), 5)    # перекладина
    if attempts < 3:
        pygame.draw.line(screen, BLACK, (300, 50), (300, 100), 5)   # веревка
    if attempts < 2:
        pygame.draw.circle(screen, BLACK, (300, 120), 20)           # голова
    if attempts < 1:
        pygame.draw.line(screen, BLACK, (300, 140), (300, 250), 5)  # тело

def main_menu():
    while True:
        screen.fill(BLUE)
        font = pygame.font.SysFont("bahnschrift", 25)
        title_surface = font.render("Welcome to Hangman!", True, WHITE)
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
    game = HangmanGame()
    clock = pygame.time.Clock()

    while True:
        screen.fill(WHITE)

        # Отображаем текущее слово с угаданными буквами
        word_display = ' '.join(letter if letter in game.guesses else '_' for letter in game.word)
        font = pygame.font.SysFont("bahnschrift", 40)
        text_surface = font.render(word_display, True, BLACK)
        screen.blit(text_surface, [WIDTH / 4, HEIGHT / 4])

        # Отображаем количество оставшихся попыток и рисуем виселицу
        attempts_surface = font.render(f'Attempts left: {game.attempts_left}', True, BLACK)
        screen.blit(attempts_surface, [10, HEIGHT - 50])
        
        draw_hangman(game.attempts_left)

        if game.game_over:
            result_text = "You win!" if game.check_win() else "You lose!"
            result_surface = font.render(result_text, True, RED)
            screen.blit(result_surface, [WIDTH / 3, HEIGHT / 2])
            scores = load_scores()
            scores[name] = max(scores.get(name, 0), game.score)
            save_scores(scores)

            # Перезапуск игры после окончания
            game.reset()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
                
                if event.unicode and event.unicode.isalpha() and len(event.unicode) == 1:
                    game.guess(event.unicode.upper())
                    if game.check_win() or game.attempts_left <= 0:
                        game.game_over = True

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main_menu()
    pygame.quit()
