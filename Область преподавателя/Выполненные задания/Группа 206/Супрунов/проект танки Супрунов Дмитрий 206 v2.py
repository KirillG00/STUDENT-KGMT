import pygame
import random
import json

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
FPS = 60
TANK_SIZE = 40
BULLET_SIZE = 5
ENEMY_SIZE = 40
FONT_SIZE = 36
PLAYER_SPEED = 5
ENEMY_SPEED = 1000
BULLET_SPEED = 5
MAX_BULLETS = 1
RELOAD_TIME = 5 # Время перезарядки в миллисекундах

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Классы игры

class Tank:
    """Класс для танка игрока."""
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)  # Прямоугольник для танка
        self.last_shot_time = pygame.time.get_ticks()  # Время последнего выстрела
        self.bullets = []  # Список пуль

    def move(self, dx, dy):
        """Перемещение танка."""
        self.rect.x += dx * PLAYER_SPEED
        self.rect.y += dy * PLAYER_SPEED

    def shoot(self):
        """Выстрел из танка."""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > RELOAD_TIME and len(self.bullets) < MAX_BULLETS:
            bullet = Bullet(self.rect.centerx, self.rect.centery)  # Создание пули
            self.bullets.append(bullet)  # Добавление пули в список
            self.last_shot_time = current_time  # Обновление времени последнего выстрела

    def draw(self, screen):
        """Отрисовка танка и его пуль."""
        pygame.draw.rect(screen, GREEN, self.rect)  # Отрисовка танка
        for bullet in self.bullets:
            bullet.draw(screen)  # Отрисовка каждой пули

class Bullet:
    """Класс для пуль."""
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 5, 5)  # Прямоугольник для пули

    def update(self):
        """Обновление положения пули."""
        self.rect.x += BULLET_SPEED

    def draw(self, screen):
        """Отрисовка пули."""
        pygame.draw.rect(screen, RED, self.rect)  # Отрисовка пули

class Enemy:
    """Класс для врагов."""
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)  # Прямоугольник для врага

    def move(self):
        """Случайное движение врага."""
        self.rect.x += random.choice([-ENEMY_SPEED, ENEMY_SPEED])
        self.rect.y += random.choice([-ENEMY_SPEED, ENEMY_SPEED])

    def draw(self, screen):
        """Отрисовка врага."""
        pygame.draw.rect(screen, BLACK, self.rect)  # Отрисовка врага
# Класс Танка
class Tank:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TANK_SIZE, TANK_SIZE)
        self.health = 100
        self.score = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, surface):
        pygame.draw.rect(surface, GREEN if self.health > 0 else RED, self.rect)

# Класс Пули
class Bullet:
    def __init__(self, x, y, direction):
        self.rect = pygame.Rect(x, y, BULLET_SIZE, BULLET_SIZE)
        self.direction = direction

    def move(self):
        if self.direction == 'UP':
            self.rect.y -= 10
        elif self.direction == 'DOWN':
            self.rect.y += 10
        elif self.direction == 'LEFT':
            self.rect.x -= 10
        elif self.direction == 'RIGHT':
            self.rect.x += 10

    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, self.rect)

# Класс Врага
class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), random.randint(0, HEIGHT - ENEMY_SIZE), ENEMY_SIZE, ENEMY_SIZE)
        self.speed = random.randint(1, 3)
        self.shoot_timer = 0

    def move(self):
        # Простая логика движения: перемещение в случайном направлении
        direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
        if direction == 'UP':
            self.rect.y -= self.speed
        elif direction == 'DOWN':
            self.rect.y += self.speed
        elif direction == 'LEFT':
            self.rect.x -= self.speed
        elif direction == 'RIGHT':
            self.rect.x += self.speed

        # Ограничение движения врага в пределах экрана
        if self.rect.x < 0: self.rect.x = 0
        if self.rect.x > WIDTH - ENEMY_SIZE: self.rect.x = WIDTH - ENEMY_SIZE
        if self.rect.y < 0: self.rect.y = 0
        if self.rect.y > HEIGHT - ENEMY_SIZE: self.rect.y = HEIGHT - ENEMY_SIZE

    def shoot(self):
        # Логика стрельбы врага
        if random.random() < 0.02:  # 2% шанс выстрела за кадр
            return Bullet(self.rect.centerx - BULLET_SIZE // 2,
                          self.rect.centery - BULLET_SIZE // 2,
                          random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT']))
        return None

    def draw(self, surface):
        pygame.draw.rect(surface, BLUE, self.rect)

# Функция для отображения текста
def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, BLACK)
    surface.blit(text_surface, (x, y))

# Меню начала игры
def show_start_menu(screen):
    screen.fill(WHITE)
    draw_text(screen, "Танчики", 60, WIDTH // 2 - 100, HEIGHT // 2 - 50)
    draw_text(screen, "Нажмите ENTER для начала", FONT_SIZE, WIDTH // 2 - 150, HEIGHT // 2 + 20)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

# Экран окончания игры
def show_game_over(screen, score):
    screen.fill(WHITE)
    draw_text(screen, "Игра окончена", 60, WIDTH // 2 - 150, HEIGHT // 2 - 50)
    draw_text(screen, f"Ваши очки: {score}", FONT_SIZE, WIDTH // 2 - 100, HEIGHT // 2 + 20)
    draw_text(screen, "Нажмите ENTER для выхода", FONT_SIZE, WIDTH // 2 - 150, HEIGHT // 2 + 60)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False

# Сохранение результатов игры
def save_score(score):
    with open("scores.json", "a") as f:
        json.dump({"score": score}, f)
        f.write("\n")

# Загрузка результатов игры
def load_scores():
    try:
        with open("scores.json", "r") as f:
            scores = [json.loads(line) for line in f]
            return scores
    except FileNotFoundError:
        return []

# Главная функция игры
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Танчики")
    clock = pygame.time.Clock()

    tank = Tank(WIDTH // 2, HEIGHT // 2)
    enemies = []
    bullets = []
    enemy_bullets = []
    level = 1
    enemy_count = 5
    bullet_direction = ''

    show_start_menu(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            tank.move(-5, 0)
        if keys[pygame.K_d]:
            tank.move(5, 0)
        if keys[pygame.K_w]:
            tank.move(0, -5)
        if keys[pygame.K_s]:
            tank.move(0, 5)
        # Стрельба танка
        if keys[pygame.K_UP]:
            bullet_direction = 'UP'
        if keys[pygame.K_DOWN]:
            bullet_direction = 'DOWN'
        if keys[pygame.K_LEFT]:
            bullet_direction = 'LEFT'
        if keys[pygame.K_RIGHT]:
            bullet_direction = 'RIGHT'

        # Ограничение движения танка в пределах экрана
        tank.rect.clamp_ip(screen.get_rect())

        # Генерация врагов на новом уровне
        if len(enemies) < enemy_count:
            enemies.append(Enemy())

        # Проверка столкновений с врагами
        for enemy in enemies[:]:
            if tank.rect.colliderect(enemy.rect):
                tank.health -= 1
                enemies.remove(enemy)
                tank.score += 10

            enemy.move()
            enemy_bullet = enemy.shoot()
            if enemy_bullet:
                enemy_bullets.append(enemy_bullet)

        # Движение пуль врагов и проверка столкновений с танком
        for enemy_bullet in enemy_bullets[:]:
            enemy_bullet.move()
            if enemy_bullet.rect.colliderect(tank.rect):
                tank.health -= 1
                enemy_bullets.remove(enemy_bullet)

            # Удаление пули за пределами экрана
            if enemy_bullet.rect.x < 0 or enemy_bullet.rect.x > WIDTH or enemy_bullet.rect.y < 0 or enemy_bullet.rect.y > HEIGHT:
                enemy_bullets.remove(enemy_bullet)

            if bullet_direction:
                bullets.append(Bullet(tank.rect.centerx - BULLET_SIZE // 2,
                                        tank.rect.centery - BULLET_SIZE // 2,
                                        bullet_direction))
                bullet_direction =''

        # Движение пуль и проверка столкновений с врагами
        for bullet in bullets[:]:
            bullet.move()
            for enemy in enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    tank.score += 20

            # Удаление пули за пределами экрана
            if bullet.rect.x < 0 or bullet.rect.x > WIDTH or bullet.rect.y < 0 or bullet.rect.y > HEIGHT:
                bullets.remove(bullet)

        # Увеличение уровня
        if len(enemies) == 0 and tank.health > 0:
            level += 1
            enemy_count += 2
            print(f"Уровень {level} начался!")

        # Проверка окончания игры
        if tank.health <= 0:
            save_score(tank.score)
            show_game_over(screen, tank.score)
            running = False

        # Обновление экрана
        screen.fill(WHITE)
        tank.draw(screen)

        for enemy in enemies:
            enemy.draw(screen)

        for bullet in bullets:
            bullet.draw(screen)

        for enemy_bullet in enemy_bullets:
            enemy_bullet.draw(screen)

        # Отображение очков и здоровья
        draw_text(screen, f"Очки: {tank.score} Здоровье: {tank.health}", FONT_SIZE, 10, 10)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()