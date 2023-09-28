first = {'roman', 'seth', 'john', 'triple', 9.2, True, 0, 1, 2, 3}
second = {'black', 'blue', 'pink', 'red'}
me = first.union(second)
for a in me:
    print(a)
first.update(second)
for b in me:
    print(b)
#14 marks for Christian Onwuka