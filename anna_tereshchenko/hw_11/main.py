from func import Calculator

calc = Calculator()


def calculation(option, x, y):
    if option == 1:
        return print(f'Результат сложения = {calc.sum(x, y)}')
    elif option == 2:
        return print(f'Результат вычитания = {calc.subtraction(x, y)}')
    elif option == 3:
        return print(f'Результат умножения = {calc.multiplication(x, y)}')
    elif option == 4:
        return print(f'Результат деления = {calc.division(x, y)}')


while True:
    try:
        option = int(input('1. Сложение\n2. Вычитание\n3. Умножение\n'
                           '4. Деление\nВведите номер пункта меню:\n'))
        if not 1 <= option <= 4:
            print('Введите число от 1 до 4: ')
            continue
    except ValueError:
        print('Это не число, пожалуйста, введите число')
        continue
    break

first_number = ''

while True:
    try:
        if not first_number:
            first_number = float(input('Введите первое число: '))
        second_number = float(input('Введите второе число: '))
        if option == 4 and second_number == 0:
            print('Делитель не может быть 0, пожалуйста, введите другое число')
            continue
    except ValueError:
        print('Это не число, пожалуйста, введите число')
        continue
    break


calculation(option, first_number, second_number)
