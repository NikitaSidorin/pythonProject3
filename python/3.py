def div(*args):

    try:
        arg1 = int(input(" Введите Делимое "))
        arg2 = int(input("Введите Делитель "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return "На ноль делить нельзя!"

    return res

    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Значение не может быть равно нулю")

print(f'result  {div()}')

 

# задание 2
def print_user(name, surname, year, city, email, phone):
    print(f"Пользователь {name} {surname} {year}-го года рождения, из города {city}, "
          f"имеет  Email {email} и телефон {phone}")


user_template = {
    'name': 'Имя',
    'surname': 'Фамилия',
    'year': 'Год рождения',
    'city': 'Город ',
    'email': 'Email',
    'phone': 'Телефон'
}
my_user = {}
for key, value in user_template.items():
    input_value = input(f'{value}: ')
    my_user.update({key: input_value})

print_user(**my_user)

# Задание 3

def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    elif arg1 < arg2 and arg2 < arg3:
        return arg2 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("1-ый argument ")), int(input("2-ой argument ")), int(input("3-ий argument ")))}')


# Задание 4
def my_func(x, y):
    if y == 0:
        return 1
    y = abs(y)
    return x * my_func(x, y-1)


while True:
    try:
        x = float(input("Введите действительное положительное число x: "))
        if x < 0:
            raise Exception()
        y = int(input("Введите целое отрицательное число y: "))
        if y > 0:
            raise Exception()
        print(1 / my_func(x, y))
        break
    except Exception as e:
        print('Неверный формат')


# задание 5

def my_sum ():
    sum_res = 0
    ex = False
    while ex == False:
        number = input('Input numbers or W for quit - ').split()

        res = 0
        for el in range(len(number)):
            if number[el] == 'w' or number[el] == 'W':
                ex = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Current sum is {sum_res}')
    print(f'Your final sum is {sum_res}')
my_sum()