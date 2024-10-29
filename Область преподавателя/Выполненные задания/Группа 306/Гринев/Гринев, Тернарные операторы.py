from datetime import datetime


today = datetime.now().strftime("%d/%m")


birthday = input("Введите вашу дату рождения (дд/мм): ").strip()

# Поздравление с днём рождения или благодарность
message = "С днём рождения! Спасибо за информацию." if birthday == today else "Спасибо за информацию."

print(message)

input()