# from random import *
# number = "123456789"
# new_str = "qwertyuiopasdfghjklzxcvbnm"
# up_str = new_str.upper()
# passw = number+new_str+up_str
# List = list(passw)
# shuffle(List)
# user_passw = ''.join([choice(List) for x in range(8)])
# print(user_passw)

import random
s1 = "ABCDEFGHIJKLMNOPQRSWXYZ"
s2 = "abcdefghijklmnopqrswxyz"
s3 = "0123456789"
s4 = "!@#$%^&*()"
s = s1+s2+s3+s4
password = ""
for i in range(15):
    password += random.choice(s)
print(password)