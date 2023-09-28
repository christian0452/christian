fruits = ['orange','orange', 'watermelon', 'pineapple', 'grapes',40]
pascal = ('orange', 'watermelon', 'pineapple', 'grapes',30)
clinton = {'orange', 'watermelon', 'pineapple', 'grapes',20}
chris120 = {
'fruitss' : 'orange',
'fruitsss' : 'watermelon',
'myfruits' : 'pineapple',
'mifruit' : 'grapes',
'age' :20
}
fruits[1] ='orange'
fruits.append('guava')
x =fruits.count('orange')
#i want to convert from tuple to a list
mynewLst = list(pascal)
#conversion has been done
#append mynewlist to fruits
fruits.extend(mynewLst)
print(fruits)
x = fruits.index('watermelon')
print(x)
fruits.insert(4, 'pineapple')
print(fruits)
fruits.pop(1)
print(fruits)