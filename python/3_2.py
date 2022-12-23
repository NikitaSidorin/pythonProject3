#задание 1
from functools import reduce
from math import factorial


def simple_calc():
    x = float(input('Введите количество отработанных часов : '))
    y = float(input('Введите суммы оплаты труда за 1 час : '))
    c = float(input('Укажите размер премии - '))
    pay = x * y
    return pay + c
print(f'Размер заработной платы составил: {simple_calc() }')




#Задание2 
result__list =[]
list = [int(i) for i in input("Введите список чисел").split()]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (result__list.append(list[i]))
print("Исходный список:", list)
print("Список, элементы которого больше предыдущего:+", result__list)   


#Задание3 
list = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]

print("Список чисел кратных 20 или 21 в диапозоне[20, 240)", list)



#Задание4
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print("Исходные элементы списка:\n", my_list)
new_list = [i for i in my_list if my_list.count(i) == 1]
print("Элементы списка, не имеющие повторений:\n", new_list)


#Задание5 
list = [i for i in range(100, 1001, 2)]
print("Список чётных чисел в диапазоне [100..1000]:\n", list)
print("Произведение всех элементов списка:\n", reduce(lambda x,y: x*y, list))



#Задание6





#задан
def factorial_gen(n):
    for i in range(n):
        print(i, end='! = ')
        yield factorial(i)

print("<<Программа вычисления факториала числа>>")
for el in factorial_gen(20):
    print(el)