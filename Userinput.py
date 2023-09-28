#we want to create user login
import string


username = input('enter your username :')
print('your username is' , username)
password = int(input('enter your password :'))
print('your password is' , password)
if password < 10:
    print('password is not sufficient')
else:
    print('password is sufficient')