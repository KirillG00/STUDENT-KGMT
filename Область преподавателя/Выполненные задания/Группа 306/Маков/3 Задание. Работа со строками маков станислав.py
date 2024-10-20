
today = date tnow().strftime("%d/%m")

birthday = input("Введите вашу дату рождения (дд/мм): ")

message = (
    f"Поздравляем с днём рождения! Спасибо за информацию."
    if birthday == today
    else "Спасибо за информацию."
)
print(message)