s = 0
N = int(input('Введите количество чисел в последовательности: '))
for i in range(N):
   a = int(input())
   s += a
print("Середнє арифметичне:", s/N)
print("Cумма всіх чисел:", s)
