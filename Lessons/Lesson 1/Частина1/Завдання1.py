a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))
d = input("Що ви хочете? + | * ")

if d == "+":
    print("Додавання становить: ", a+b+c)

elif d == "*":
    print("Множення становить: ", a*b*c)

else:
    print("Такого варіанту немає, спробуйте ще раз.")

End = input()







#Задание 1
#Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
#на экран сумму трёх чисел или произведение трёх чисел.