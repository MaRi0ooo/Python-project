import random
user = input("Enter your name: ")
print(f"Welcome: {user}")
a = input("Select level: easy | normal | hard | insane ")

for i in range(1, 10+1):
    if a == "easy":
        print(random.randint(1, 5), "*", random.randint(1, 5), "=")
        int(input())

for i in range(1, 10+1):
    if a == "normal":
        print(random.randint(1, 8), "*", random.randint(1, 8), "=")
        int(input())

for i in range(1, 10+1):
    if a == "hard":
        print(random.randint(1, 9), "*", random.randint(1, 9), "=")
        int(input())

for i in range(1, 20+1):
    if a == "insane":
        print(random.randint(1, 100), "*", random.randint(1, 100), "=")
        int(input())






''' Задание 3
Написать программу, которая проверяет пользователя
на знание таблицы умножения. Программа выводит на
экран два числа, пользователь должен ввести их произведение. Разработать несколько уровней сложности (от Практическое задание оличаются сложностью и количеством вопросов).
Вывести пользователю оценку его знаний.'''
