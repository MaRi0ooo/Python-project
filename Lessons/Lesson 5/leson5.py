a = int(input())
b = int(input())
if a > b:
    a, b = b, a
for a in range(a, b+1):
    if a % 2 == 1:
        print(a)

input()