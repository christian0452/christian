userList=[]

while True:

    username = input('enter your name :')
    age = int(input('enter your age :'))
    level = int(input('enter your level :'))
    regno = input('enter your registration number :')
    state = input('enter your state of origin :')
    email = input('enter your email address :')
    password = input('enter your password :')
    phone = input('enter your phone number :')

    if len(password)<5 and len(phone)!=11:
        print('your password should at least be 5 or your phone number should be 11')
        continue
    userList.append([username, age, level, regno, state, email, password, phone])
    print('you have completed your student information')
    break
print('user_list', userList)