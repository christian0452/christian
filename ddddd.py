
pin = int(input('enter your pin :'))
print('what do you want to do')
next = input('withdraw, balance, transfer, end :')
amount = int(input('enter your amount :'))
if amount > 20000:
    print('you have exceeded your limit')
else:
    print('take your cash')
next = input('what do you want to do next: withdraw, balance, transfer, end :') 
print('take your ATM card')