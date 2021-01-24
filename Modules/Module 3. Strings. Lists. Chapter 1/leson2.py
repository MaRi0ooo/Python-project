import re
s = input("Введіть ваш текст: ")
# Кількість букв
count = len(re.findall('[a-zA-Z]', s))
print("Кількість букв:", count)
# Кількість цифр
cnt = 0
for i in s:
    if i.isdigit():
        cnt += 1
if cnt:
    print("Кількість цифр:", cnt)
else:
    print("Цифр немає!")






