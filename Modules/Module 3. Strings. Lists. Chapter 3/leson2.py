from random import random
N = 10
even = 0
odd = 0
neg = 0
poz = 0
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 10) - 5

for i in range(N):
    if arr[i] % 2 == 0:
        even += arr[i]
    else:
        odd += arr[i]

    if arr[i] <= 0:
        neg += arr[i]
    else:
    	poz += arr[i]












print("Отрицательный: ", arr)
print("Чётный: ",even)
print("Не чётный: ",odd)
print("Положительный: ", poz)
print("Отрицательный: ", neg)




































# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")