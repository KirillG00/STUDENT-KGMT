import wave
import pygame
from numpy.compat import unicode

# Имя музыкального файла
music_file = "Frank-Sinatra-My-Funny-Valentine.wav"
# Изображение музыкального автомата
image_file = "jukebox.png"

# Инициализация Pygame
pygame.init()

# Отображение изображения музыкального автомата
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load(image_file)
screen.blit(background, (0, 0))

# Воспроизведение музыки
pygame.mixer.music.load(music_file)
pygame.mixer.music.play()

# Получение названия песни из музыкального файла
with wave.open(music_file, 'r') as f:
    song_title = f.getnframes()

# Основной игровой цикл
while pygame.mixer.music.get_busy():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()

pygame.quit()
