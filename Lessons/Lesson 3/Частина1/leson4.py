a = int(input("Впиши розмір ромба: "))

for i in range(0, a + 1):
    for index in range(0, a - i):
        print(end = " ")

    for index in range(0, i):
        print("*", end=" ")
    print()

if i == a:
    for i in range(a - 1, 0, - 1):
        for index in range(0, a - i):
            print(end=" ")

        for index in range(0, i):
            print("*", end=" ")
        print()


'''Задание 4
Вывести на экран ромб из звездочек.'''

# print("""
#  *
# ***
#  *
# """)
