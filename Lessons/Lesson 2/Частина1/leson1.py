a = int(input("Перше число: "))
b = int(input("Друге число: "))

aeven = False # ne 4etnoe
beven = False # ne 4etnoe
even = 0
odd = 0

if a % 2 == 0:
    aeven = True

if b % 2 == 0:
    beven = True

if aeven == True or beven == True:
    if aeven == True and beven == True:
        even = a+b
    else:
        if aeven == True:
            even = a
        else:
            odd = a
        if beven == True:
            even = b
        else:
            odd = b

else:
    odd = a+b

print("Сумма четных =", even) # 4etnoe
print("Сумма не четных =",odd) # ne 4etnoe
print("Сумма =", a + b) # summa
print("Арифмитическая сумма =", (a+b)/2) # average

# Задание 1
# Пользователь вводит с клавиатуры два числа. Нужно
# посчитать отдельно сумму четных, нечетных и чисел,
# кратных 9 в указанном диапазоне, а также среднеарифметическое каждой группы.