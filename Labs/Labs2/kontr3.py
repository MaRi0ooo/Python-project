maxcount = 0
count = 0
a = -1
while a != 0:
    a = int(input("Input elements: "))
    if a > maxcount:
        maxcount, count = a, 1
    elif a == maxcount:
        count += 1
print("End:", count)