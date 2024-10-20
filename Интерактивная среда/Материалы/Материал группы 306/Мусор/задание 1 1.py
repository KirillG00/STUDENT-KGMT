def calculate_wallpaper_needed():
    # Запрашиваем размеры комнаты
    length = float(input("Введите длину комнаты (в метрах): "))
    width = float(input("Введите ширину комнаты (в метрах): "))
    height = float(input("Введите высоту комнаты (в метрах): "))

    # Вычисляем периметр и площадь стен
    P = (length + width) * 2
    S_sten = P * height
    print(f"Площадь стен: {S_sten} квадратных метров")

    # Запрашиваем размеры рулона обоев
    roll_width = float(input("Введите ширину рулона обоев (в метрах): "))
    roll_length = float(input("Введите длину рулона обоев (в метрах): "))

    # Вычисляем площадь одного рулона обоев
    S_oboi = roll_width * roll_length
    print(f"Площадь одного рулона обоев: {S_oboi} квадратных метров")

    # Вычисляем количество необходимых рулонов обоев
    quantity_of_ro,lls = S_sten / S_oboi
    print(f"Количество рулонов обоев, необходимых для ремонта: {quantity_of_rolls:.2f}")

    # Дополнительное задание - стоимость рулона обоев
    cost_per_roll = float(input("Введите стоимость одного рулона обоев (в рублях): "))

    # Вычисляем общую стоимость покупки обоев
    total_cost = quantity_of_rolls * cost_per_roll
    print(f"Суммарная стоимость покупки обоев: {total_cost:.2f} рублей")


if __name__ == "__main__":
    calculate_wallpaper_needed()
пенис в жопе вазелин