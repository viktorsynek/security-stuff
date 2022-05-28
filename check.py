contains_number = False
numbers = ['1','2','3','4','5','6','7','8','9']

pw = input("Enter your password: ")

for i in pw:
    if i in numbers:
        contains_number = True
        break

if len(pw) >= 8 and contains_number == True:
    print("Password valid")

else:
    print("Password invalid!")
