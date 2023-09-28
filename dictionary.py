#dictionary type
from re import T


Thisdictionary = {
    'carcolour': 'blue',
    'size': 45,
    'numberofdoors': 4,
    'model': 'cadillac',
    'yearofproduction': 2022
}
diict = (type(Thisdictionary))
print(diict)
print(len(Thisdictionary))
results = Thisdictionary['carcolour']
print(results)
ret = Thisdictionary.get ('model')
print(ret)
res = Thisdictionary.keys()
print(res)
rev = Thisdictionary.values()
print(rev)
Thisdictionary['model'] = 'tesla'
print(Thisdictionary)
Thisdictionary['yearofproduction'] = 2024
print(Thisdictionary)
tre = Thisdictionary.keys()
print(tre)
tra = Thisdictionary.items()
print(tra)
if 'model' in Thisdictionary:
    print(True)
elif 'model' not in Thisdictionary:
    print(False)
#method for update
Thisdictionary.update({'numberofdoors': 10})
print(Thisdictionary)
Thisdictionary['steeringtype'] = 'circle'
print(Thisdictionary)
Thisdictionary['cupholdertype'] = 'oval'
print(Thisdictionary)

chris = dict(name = 'john', school = 'khemsafe', totalstudents = 15)
print(chris)
#how to access items in our dictionary
Thisdictionary.pop('yearofproduction')
print(Thisdictionary)
Thisdictionary.popitem()
print(Thisdictionary)
for x in Thisdictionary.values():
    print(x)
for y in Thisdictionary.keys():
    print(y)
for x,y in Thisdictionary.items():
    print(x,y)
fate = Thisdictionary.copy()
print(fate)
late = dict(fate)
print(late)