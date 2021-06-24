set = {1,2,3,4,5,'Hello'}
print(set)

#loop
for item in set :
    print(item)

#some methods
print(len(set))
set.add(7)
set1 = {1,2,3}
set2 = {3,4,5,66}
set.update(set2)
print(set)
set.remove('Hello')
print(set)
set_union = set1.union(set2)
set_intersection = set1.intersection(set2)
print(set_union) 
print(set_intersection)
set_symmetric = set1.symmetric_difference(set2)
print(set_symmetric)
set.clear()
print(set)
del set
print(set)