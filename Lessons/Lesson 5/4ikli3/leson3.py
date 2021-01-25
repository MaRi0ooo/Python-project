money = int(input("Введите сумму денег, которую вы хотите конвертировать: "))

USD = 28.273
EUR = 32.980
RUB = 0.328
PLN = 6.825

konvert = input("""В какую валюту вы хотите конвертировать деньги?:
        USD | EUR | RUB | PLN""")


if konvert == "USD":
       print(money * USD, "- USD")

elif konvert == "EUR":
       print(money * EUR, "- EUR")

elif konvert == "RUB":
       print(money * RUB, "- RUB")

elif konvert == "PLN":
       print(money * PLN, "- PLN")

input("Нажмите для выхода!")