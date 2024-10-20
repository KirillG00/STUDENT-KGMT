while True :
    s1 = input("Введите первое число:")
    s2 = input("Введите второе число:")
    if s1 != '' and s2 != '':
        print("Сумма чисел: ", int(s1)+int(s2))
        str = input('Нажмите Y или y для завершения программы:')
        if (str == 'Y' or str == 'y'): break
