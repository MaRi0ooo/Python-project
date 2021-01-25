from random import *

N = 30
s = []
mass = [s.append(randint(-10, 10)) for i in range(N)]
print(s)

max = -11
min = 0
for i in s:
    if i > max:
        max = i
    else:
        min = i

for i in range(len(s)):
    for j in range(N - i -1):
        if s[j] < s[j+1]:
            s[j], s[j+1] = s[j+1], s[j]
print(s)

print("max:", max)
print("min:", min)


