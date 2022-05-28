#variable assignment + imports
from random import randint
import string
lst = []
asd = 10
password = ""

# alphabet list
alphabet_string =string.ascii_lowercase + string.ascii_uppercase 
alphabet_list = list(alphabet_string)

# number list
numerical_string = list(range(48))
numerical_list = []
for i in numerical_string:
    numerical_list.append(str(i))


# opening + writing into file
for i in range(20):
    x = randint(0,47)
    passwordHashA = alphabet_list[x]
    passwordHashN = numerical_list[x]
    passwordHash = passwordHashN + passwordHashA
    password += passwordHash
    asd -= 1
    
with open("password.txt", "w+") as f:
    f.write(password)

# opening + reading the file
with open("password.txt", "r") as f:
    x = f.readlines()
    print(x)






