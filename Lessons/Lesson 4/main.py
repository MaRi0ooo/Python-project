import random
my_list = [random.randint(0, 9) for i in range(10)]
my_listt = [random.randint(-9, 9) for i in range(10)]
even = [x for x in my_list if x % 2 == 0]
odd = [j for j in my_list if j % 2 != 0]
neg = [d for d in my_listt if d <= 0]
poz = [b for b in my_list if b >= 0]
print(even)
print(odd)
print(neg)
print(poz)






'''my_list = []
for i in range(10):
    my_list.append(i)
print(my_list)'''

'''my_list = [i**2 for i in range(10)]
print(my_list)'''

'''Fn1 = 1
Fn2 = 1
for i in range(2, 10):
    Fn1, Fn2 = Fn2, Fn1 + Fn2
    print(Fn1, end=' ')'''

'''b = [int(((1+(5**0.5))**n-(1-(5**0.5))**n)/(2**n*(5**0.5))) for n in range(10)]
print(b)'''

'''a=[2**i for i in range(10)]
print(a)'''




