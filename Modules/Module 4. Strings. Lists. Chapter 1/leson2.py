user = input("Введіть строку: ")
s =[]
while True:
    user1 = input("Введыть резервне слово[1 - вихід]: ")
    if user1 == "1":
        break
    s.append(user1)
for i in s:
    for j in i:
        for x in user:
            if x == j:
                user = user.replace(x,j.upper())
print(user)

'''string = input("")
text = input("")
for i in text:
    if i == " ":
        string = string.replace(text, text.upper())
        print(string)'''

'''Пользователь вводит с клавиатуры некоторый текст,
после чего пользователь вводит список зарезервированных
слов. Необходимо найти в тексте все зарезервированные
слова и изменить их регистр на верхний. Вывести на
экран измененный текст. '''
