a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
for a in range(a, b+1):
    if a % 2 == 1:
        print(a)
input()