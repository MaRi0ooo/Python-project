a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))
d = input("Що хочете вибрати? > | < | average")


## Максимальне значення
if d == ">":
    if a>b and a>c:
        print ("Найбільше число становить: ", a)
    elif b>a and b>c:
        print ("Найбільше число становить: ", b)
    elif c>a and c>b:
        print ("Найбільше число становить: ", c)

## Мінімальне значення
elif d == "<":
    if a<b and a<c:
        print ("Найменше число становить:", a)
    elif b<a and b<c:
        print ("Найменше число становить:", b)
    elif c<a and c<b:
        print ("Найменше число становить:", c)

## average
elif d == "average":
    print((a+b+c)/3)

else:
    print("Такого варіанту немає, спробуйте ще раз.")

End = input()


#Задание 2
#Пользователь вводит с клавиатуры три числа. В зависимости от выбора пользователя программа выводит
#на экран максимум из трёх, минимум из трёх или среднеарифметическое трёх чисел.