text = input("Введіть текст: ")
cnt = 0
smb = 0
symbol = [",", ".", ":", ";"]
znk = ["!"]
z = znk.count("!")
for i in range(len(text)):
    if text[i].isnumeric():
        cnt += 1
    for j in range(len(symbol)):
        if text[i] == symbol[j]:
            smb += 1

print(text.capitalize())
print("Кількість цифр:", cnt)
print("Кількість символів:", smb)
print("Знаків оклику:", z)



