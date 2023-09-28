print('welcome to First Bank')
flly = input('select any option :')
a = "WITHDRAW"
b = "BALANCE"
c = "TRANSFER"
d = "END"
if flly is "a":
    print('choose an ammount')
    second=input("enter the ammount: ")
    i = 2000
    j = 5000
    k = 10000
    l = 20000

    if second is "i":
        print('take your cash ')
    elif second is 'j':
        print('take your cash ')
    elif second is 'k':
        print('take your cash ')
    elif second is 'l':
        print('take your cash ')
elif flly is 'b':
    print('see your balance :')
elif flly is 'c':
    print('choose an amount')
    third = input('enter the amount :')
    w = 2000
    x = 5000
    y = 10000
    z = 20000
    if third  is 'w':
        print('successfully transferred 2k')
    elif third is 'x':
        print('successfully transferred 5k')
    elif third is 'y':
        print('successfully transferred 10k')
    elif third is 'z':
        print('successfully transferred 20k')
elif flly is 'd':
    print('take your ATM card')