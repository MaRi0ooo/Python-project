from random import random

n = 500
q = 0
n = int(input("Угадай число: "))
for i in range(n):
	if int(random(n)*100) % 2 == 0:
		q += 1

	elif n < q:
		print("Число немного меньше: ")