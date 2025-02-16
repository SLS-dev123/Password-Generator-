import random
special = "!@#$%&*,.;:?"
upper = "ABCDEFGHIJKLMNOPQRSTUWVXYZ"
lower =""
for i in range(ord('a'),ord('z')+1):
    lower = lower+chr(i)
num = "0123456789"
password = ""
for j in range(2):
    i = random.randint(0,25)
    t = random.randint(0,9)
    k = random.randint(0,25)
    z = random.randint(0,11)
    password += upper[i]+lower[k]+special[z]+num[t]
print("the password is: ",password)