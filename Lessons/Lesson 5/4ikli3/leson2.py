a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))

s=0
c= int(input("Введіть число для перевірки: "))
for i in range(a,b+1):
    if i == c:
        if i == c:
            print("!", i, "!", end=" ")
            s=1
            continue
        print(i,end=" ")
    if s==1:
        break