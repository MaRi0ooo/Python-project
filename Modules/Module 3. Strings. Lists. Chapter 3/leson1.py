from random import *
from numpy import *

N = 50
even = 0
odd = 0
neg = 0
div3 = 0
massindxfirst = 0
massindxlast = 0
sumpos = 0
summaxmin = 0
A = [randint(-50, 50) for i in range(N+1)]

for i in range(N):
    if A[i] % 2 == 0:
        even += A[i]
    else:
        odd += A[i]

    if A[i] <= 0:
        neg += A[i]

    if i % 3 == 0:
        div3 += A[i]

    if A[i] >= 0:
        if massindxfirst == 0:
            massindxfirst = i
        else:
            massindxlast = i
for massindxfirst in range(massindxlast):
    sumpos += A[massindxfirst]
i = A.index(min(A))

for i in range(A.index(max(A))):
    summaxmin += A[i]

print("Сумма чётных: ", even)
print("Сумма не чётных: ", odd)
print("Сумма негативных: ", neg)
print("Cумма между минимальным и максимальным элементом: ", summaxmin)
print("Cумма первого и последнего положительного элемента: ", sumpos)