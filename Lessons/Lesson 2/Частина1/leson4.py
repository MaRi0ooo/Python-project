from numpy import *
from array import *

count = 10
num_array = array('i', [])

for i in range(count):
    num_array.append(int(input("Введите числа: ")))
    if num_array[i] == 7:
        exit()

print("Максимальне =", max(num_array))
print("Минимальне =", min(num_array))
print("Сумма =", sum(num_array))
print("Кількість введеня =", count)






# Задание 4
# Пользователь вводит с клавиатуры числа. Программа должна подсчитывать сумму, максимум и минимум,
# введенных чисел. Когда пользователь вводит число 7
# программа прекращает свою работу и выводит на экран
# надпись «Good bye!»