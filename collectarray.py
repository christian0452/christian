mylist = ["apple", "banana", "cherry", 1, "apple"]
print(mylist)
print(len(mylist))
print(mylist[1])
print(mylist[3])
print(mylist[1:])
mylist[4] = "orange"
print(mylist)
if "orange" in mylist:
    print(True)
else:
    print(False)
thislist = ["chris", "mike", 2, 3, False]
mylist.append(thislist)
print(mylist)
mylist.clear()
print(mylist)