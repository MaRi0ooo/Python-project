import random

myList = [0]*25
poz = 0
neg = 0
nuli = 0

for i in range(20):
	myList[i] = random.randrange(-15, 15)

for i in myList:
	if i<0:
		poz += 1
	elif i == 0:
		nuli += 1
	else:
		neg += 1

minn = min(myList)
maxx = max(myList)
print(myList)
print(f'''Позитивні числа: {poz}
Негативні числа: {neg}
Максимальне число: {maxx}
Мінімальне число: {minn}
Кількість нулів: {nuli}''')