import pygame
import json
import os
import random

# Инициализация Pygame
pygame.init()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 153, 213)

# Размеры экрана
WIDTH = 600
HEIGHT = 400

# Настройка экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rock-Paper-Scissors Game')

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

def main_menu():
    while True:
        screen.fill(BLUE)
        font = pygame.font.SysFont("bahnschrift", 25)
        title_surface = font.render("Welcome to Rock-Paper-Scissors!", True, WHITE)
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

def display_result(player_choice, computer_choice, result):
    screen.fill(BLUE)
    font = pygame.font.SysFont("bahnschrift", 30)
    result_surface = font.render(f'You chose: {player_choice}', True, WHITE)
    computer_surface = font.render(f'Computer chose: {computer_choice}', True, WHITE)
    outcome_surface = font.render(f'Result: {result}', True, WHITE)

    screen.blit(result_surface, [WIDTH / 4, HEIGHT / 4])
    screen.blit(computer_surface, [WIDTH / 4, HEIGHT / 2])
    screen.blit(outcome_surface, [WIDTH / 4, HEIGHT * 3 / 4])

    pygame.display.update()
    pygame.time.delay(2000)  # Задержка перед следующей игрой

def game_loop(name):
    choices = ["Rock", "Paper", "Scissors"]
    score = 0
    high_score_data = load_scores()
    high_score = high_score_data.get(name, 0)

    while True:
        screen.fill(BLUE)
        font = pygame.font.SysFont("bahnschrift", 25)
        instruction_surface = font.render("Choose: R (Rock), P (Paper), S (Scissors)", True, WHITE)
        score_surface = font.render(f'Score: {score} | High Score: {high_score}', True, WHITE)

        screen.blit(instruction_surface, [WIDTH / 6, HEIGHT / 4])
        screen.blit(score_surface, [WIDTH / 6, HEIGHT / 3])

        pygame.display.update()

        player_choice = None
        
        while player_choice is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        player_choice = "Rock"
                    elif event.key == pygame.K_p:
                        player_choice = "Paper"
                    elif event.key == pygame.K_s:
                        player_choice = "Scissors"
                    elif event.key == pygame.K_ESCAPE:
                        return

            # Проверка на выход из игры
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        computer_choice = random.choice(choices)

        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "Rock" and computer_choice == "Scissors") or
             (player_choice == "Paper" and computer_choice == "Rock") or
             (player_choice == "Scissors" and computer_choice == "Paper")
        result = "You win!"
        score += 1
        else:
        result = "You lose!"
        score -= 1

        display_result(player_choice, computer_choice, result)

        # Сохраняем рекорд
        if score > high_score:
            high_score_data[name] = score
            save_scores(high_score_data)

if __name__ == "__main__":
    main_menu()
    pygame.quit()
