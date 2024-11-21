import pygame #Импортируем библиотеку Pygame, которая используется для создания игр и работы с графикой.
import random #Импортируем модуль `random`, который позволяет генерировать случайные числа, что полезно для размещения еды.

#Определяем константы для ширины и высоты экрана, а также для размера блока змейки и еды. Эти значения можно изменить, чтобы изменить размеры игры.
SCREEN_WIDTH = 800 # Ширина экрана
SCREEN_HEIGHT = 600 # Высота экрана
BLOCK_SIZE = 20 # ширина змейки


class Animal: #Создаем базовый класс "Animal", который будет представлять общее животное.

    def __init__(self, name): # В конструкторе "__init__" класса "Animal" определяем атрибут "name", который хранит имя животного.
        self.name = name

    def make_sound(self): #Метод `make_sound` предназначен для вывода звука животного.

        raise NotImplementedError("Этот метод должен быть переопределен") #Он будет переопределен в подклассах. Используем "raise NotImplementedError", чтобы указать, что этот метод должен быть реализован в дочерних классах.


class Snake(Animal): #Создаем класс "Snake", который наследует от класса "Animal". Это означает, что "Snake" будет иметь все атрибуты и методы "Animal".

    def __init__(self): #В конструкторе класса `Snake` вызываем конструктор базового класса "Animal" с именем "Snake".
        super().__init__("Snake")
        self.positions = [(100, 100), (80, 100), (60, 100)]  #"self.positions" хранит список координат блоков змейки. Начальная позиция состоит из трех сегментов.
        self.direction = (BLOCK_SIZE, 0)  #"self.direction" определяет текущую скорость и направление движения змейки. Начальное направление — вправо.
        self.grow_flag = False  #"self.grow_flag" — это флаг, указывающий, будет ли змейка расти после поедания еды.

    def change_direction(self, direction): #Метод change_direction принимает новое направление в виде кортежа.
        """Изменение направления змейки."""
        if (direction[0] * -1, direction[1] * -1) != self.direction: #Проверяем, что новое направление не противоположно текущему (чтобы избежать столкновения со своим телом). Если это так, обновляем направление.

            self.direction = direction

    def move(self): #Метод "move" отвечает за перемещение змейки.
        """Движение змейки."""
        head_x, head_y = self.positions[0] #Получаем текущие координаты головы змейки и вычисляем новые координаты головы на основе направления.
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        self.positions.insert(0, new_head)

        if not self.grow_flag: #Если змейка не должна расти, удаляем последний элемент из списка, чтобы она не удлинялась.
            self.positions.pop()  # Удалить последний элемент
        else:
            self.grow_flag = False  # Сбросить флаг после роста

    def grow(self):  #Метод "grow" устанавливает флаг "grow_flag" в "True", чтобы при следующем перемещении змейка удлинилась.
        """Увеличение змейки."""
        self.grow_flag = True

    def draw(self, surface):  #Метод "draw" отрисовывает змейку на переданном объекте "surface" (поверхности экрана). Каждый сегмент змейки рисуется как зеленый квадрат.
        """Отрисовка змейки на экране."""
        for pos in self.positions:
            pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))


class Food: #Создаем класс "Food", который отвечает за еду для змейки.
    def __init__(self):
        self.position = (0, 0)
        self.spawn_food() #В конструкторе инициализируем позицию еды и вызываем метод "spawn_food()" для размещения еды на экране.

    def spawn_food(self): #Метод "spawn_food" устанавливает случайную позицию еды, чтобы она появлялась в пределах игрового экрана.
        """Спавн еды в случайном месте."""
        self.position = (random.randint(0, (SCREEN_WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                         random.randint(0, (SCREEN_HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)

    def draw(self, surface): #Метод "draw" отрисовывает еду на экране в виде красного квадрата.
        """Отрисовка еды на экране."""
        pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))


class Game:    #Создаем класс "Game", который управляет игровым процессом. В конструкторе создаем экземпляры змейки и еды, устанавливаем счет, часы и флаг для управления игрой.
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.clock = pygame.time.Clock()
        self.running = True

    def check_collision(self): #Метод "check_collision" проверяет, съела ли змейка еду. Если да, увеличиваем змейку и спавним новую еду, а также увеличиваем счет.
        """Проверка коллизии между змейкой и едой."""
        if self.snake.positions[0] == self.food.position:
            self.snake.grow()
            self.food.spawn_food()
            self.score += 1

    def run(self):  #етод "run" инициализирует Pygame, создает экран и устанавливает заголовок окна.
        """Основной игровой цикл."""
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption
        
        while self.running:   #Основной игровой цикл, который обрабатывает события. Если пользователь закрывает окно, игра завершается. Если нажаты клавиши, меняется направление змейки.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction((0, -BLOCK_SIZE))
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction((0, BLOCK_SIZE))
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction((-BLOCK_SIZE, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction((BLOCK_SIZE, 0))

            self.snake.move() #Обновляем положение змейки и проверяем коллизии с едой.
            self.check_collision()

            # Отрисовка
            screen.fill((0, 0, 0))  # Очистка экрана
            self.snake.draw(screen)
            self.food.draw(screen)
            pygame.display.flip()  # Обновление экрана
            self.clock.tick(15)  # Установка FPS

        pygame.quit() #Завершаем работу Pygame.

# Запуск игры
if __name__ == "__main__":
    Game().run() 




#Управление:
#Стрелка вверх: Двигать змейку вверх.
#Стрелка вниз: Двигать змейку вниз.
#Стрелка влево: Двигать змейку влево.
#Стрелка вправо: Двигать змейку вправо.




#Инкапсуляция
#Атрибуты и методы внутри классов "Snake" и "Food" защищают внутреннее состояние объекта от непосредственного доступа извне.
#Например, состояние змейки и еды хранится внутри соответствующих классов.

#Наследование 
#Класс "Snake" наследует от базового класса "Animal". Это позволяет расширить функциональность, если вы захотите добавить другие животные.

#В данном примере можно добавить различные классы животных, которые будут наследовать от "Animal" и иметь свои специфические методы.
#Например, можно создать класс "Tiger", который будет иметь метод "roar()"".