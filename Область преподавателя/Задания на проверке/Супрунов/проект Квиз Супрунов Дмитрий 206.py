import pygame
import json
import os

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
pygame.display.set_caption('Quiz Application')

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
        title_surface = font.render("Welcome to Quiz Application!", True, WHITE)
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

def display_question(question, options):
    screen.fill(BLUE)
    font = pygame.font.SysFont("bahnschrift", 25)
    question_surface = font.render(question, True, WHITE)
    screen.blit(question_surface, [20, 20])

    for i, option in enumerate(options):
        option_surface = font.render(f"{i + 1}. {option}", True, WHITE)
        screen.blit(option_surface, [20, 60 + i * 40])

    pygame.display.update()

def game_loop(name):
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Lisbon"],
            "answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "answer": "4"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
            "answer": "Pacific"
        }
    ]

    score = 0
    high_score_data = load_scores()
    high_score = high_score_data.get(name, 0)

    for q in questions:
        display_question(q["question"], q["options"])

        answered = False
        while not answered:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4]:
                        selected_option = event.unicode
                        selected_answer = q["options"][int(selected_option) - 1]

                        if selected_answer == q["answer"]:
                            score += 1
                        answered = True
            
            # Проверка на выход из игры
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

    # Сохраняем рекорд
    if score > high_score:
        high_score_data[name] = score
        save_scores(high_score_data)

    # Показать результаты
    show_results(score, high_score)

def show_results(score, high_score):
    while True:
        screen.fill(BLUE)
        font = pygame.font.SysFont("bahnschrift", 30)
        result_surface = font.render(f'Your Score: {score}', True, WHITE)
        high_score_surface = font.render(f'High Score: {high_score}', True, WHITE)
        instruction_surface = font.render("Press ENTER to restart or ESC to exit", True, WHITE)

        screen.blit(result_surface, [WIDTH / 4, HEIGHT / 3])
        screen.blit(high_score_surface, [WIDTH / 4, HEIGHT / 2])
        screen.blit(instruction_surface, [WIDTH / 6, HEIGHT / 2 + 40])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                elif event.key == pygame.K_ESCAPE:
                    return False

if __name__ == "__main__":
    main_menu()
    pygame.quit()
