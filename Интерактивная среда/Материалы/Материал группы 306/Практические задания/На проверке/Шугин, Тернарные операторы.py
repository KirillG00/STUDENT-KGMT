from datetime import datetime

# Получаем текущую дату
today = datetime.now().strftime("%d/%m")

# Запрашиваем у пользователя дату рождения
birthday = input("Введите вашу дату рождения (дд/мм): ").strip()

# Поздравление с днём рождения или благодарность
message = "С днём рождения! Спасибо за информацию." if birthday == today else "Спасибо за информацию."

# Выводим сообщение
print(message)

input()