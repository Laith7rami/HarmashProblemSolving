import string
import random

upper = list(string.ascii_uppercase)
lower = list(string.ascii_lowercase)
number = list(string.digits)
pun = list(string.punctuation)
random.shuffle(upper)
random.shuffle(lower)
random.shuffle(number)
random.shuffle(pun)
n = input("how many charectar is password: ")

while True:
    try:
        n = int(n)
        if n < 6:
            print("most password is hight 6 car")
            n = input("how many charectar is password")
        else:
            break

    except:
        print(" the input is not numbers")
        n = input("how many charectar is password")

alpha = round(n * 0.3)
pun_num = round(n * 0.2)
print(alpha,"\n",pun_num)
password = []
for i in range(alpha):
    password.append(upper[i])
    password.append(lower[i])
for i in range(pun_num):
    password.append(number[random.randint(0,9)])
    password.append(pun[i])
random.shuffle(password)
password = "".join(password)

print(password)



