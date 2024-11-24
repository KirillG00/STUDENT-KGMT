#рандом
import random
integer = random.randint(1, 10) #Число, сгенерированное программой
attempt = 0

while True:
    print("Я загадал число от 1 до 10, :)")
    user_num = int(input("Ваша догадка: "))
    attempt += 1
    if user_num == integer:
        print("Ты угадал число")
        break
    elif user_num > integer:
        print("Мое число меньше")
    elif user_num < integer:
        print("Мое число больше")
        
input()