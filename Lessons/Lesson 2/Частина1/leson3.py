running = True

while running:
    guess = int(input("Введите число: "))
    if guess == 7:
        running = False

    elif guess > 0:
        print("«Number is positive»")
        print("Напишите цифру 7 что бы закончить цикл!")

    elif guess == 0:
        print("«Number is equal to zero»")
        print("Напишите цифру 7 что бы закончить цикл!")

    else:
        print("«Number is negative»")
        print("Напишите цифру 7 что бы закончить цикл!")

print("Good bye!")


# Задание 3
# Пользователь вводит с клавиатуры числа. Если число
# больше нуля нужно вывести надпись «Number is positive»,
# если меньше нуля «Number is negative», если равно нулю
# «Number is equal to zero». Когда пользователь вводит
# число 7 программа прекращает свою работу и выводит
# на экран надпись «Good bye!»