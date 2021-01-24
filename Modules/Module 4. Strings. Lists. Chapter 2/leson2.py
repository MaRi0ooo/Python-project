N = int(input("Скільки буде чисел?: "))
b = int(input("Яку цифру считати?: "))
cnt = 0
for i in range(1, N + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == b:
            cnt += 1
        m = m // 10

print("Було введено %d цифр %d" % (cnt, b))