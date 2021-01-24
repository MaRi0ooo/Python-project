user = input("Введіть строку: ")
space = 0
dots = 0
for i in user:
    if i == "." or i == "!" or i == "?":
        space+=1
if user.count("..."):
    dots+=1
space= space - (dots*2)
print("К-сть речень: ", space)

'''Есть некоторый текст. Посчитайте в этом тексте количество предложений и выведите на экран полученный
результат.'''