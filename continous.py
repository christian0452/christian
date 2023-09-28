#python operators
# Arithmetic operators 
#Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Aritmetic operators eg:
# Addition(+)
# Subtraction(-)
# Multiplication(*)
# Division(/)
# Modulus(%)
# Exponentiation(**)
# Floor division(//)

a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

# Assignment operators eg;
# Equal to(=)
# Addition and equal to(+=)
# Subtraction and equal to(-=)
# Multiplication and equal to(*=)
# Division and equal to(/=)
# Modulus and equal to(%=)

c = 20
c += 30
d = 20
d -= 25
e = 10
e *= 3
f = 15
f /= 3
g = 17
g %= 5
print(c)
print(d)
print(e)
print(f)
print(g)

# Comparison operator eg;
# Equal(==)
# Not equal(!=)
# Greater than(>)
# Less than(<)
# Greater than or egual to(>=)
# Less than or equal to(<=)

h = 25
i = 4
print(h==i)
print(h!=i)
print(h>i)
print(h<i)
print(h>=i)
print(h<=i)

# Logical operators eg;
# and: Returns True if both statemants are True
# or: Returns True if one of the statements is True
# not: Reverse the result, returns false if the result is True

j = 5
k = 8
print("my result is false", j<4 and k<9)
print("my result is true",j==5 and k==8)
print("my resukt is true", j<4 or k<9)
print("my result is true", not(j<4 and k<9))
print("my result is true", k>1 and j>3, 
      "\nmy result is ",not(k>1 and j>3))

# Identity operators eg;
# is: Returns True if both variables are the same object
# is not: Returns True if both variables are not the same object

l = 20
m = l
print(l is m)
print(l is not m)

# Membership operators eg;
# in: Returns True if a sequence with the specified value is present in the object
# not in: Returns True if a sequence with the specified value is not present in the object

n = 'apple'
print('apple' in n)
print('apple' not in n)
fruits = 'banana'
print('banana' in fruits)
print('banana' not in fruits)
if 'banana' in fruits:
    myfruits = fruits.upper()
    print(myfruits, len(myfruits))
