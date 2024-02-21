# set will not allowed duplicate items
t = ("TheTestingAcademy", "for", "TheTestingAcademy")
print(set(t))

# union of two sets - combines two set items
set1 = {1,2,3,4}
set2 = {5,6,7,8}
my_set = set1.union(set2)
print(my_set)

# Intersection of two sets - common items it prints
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.intersection(set2)
print(my_set)

# difference of two sets - except common items it prints from first set
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.difference(set2)
my_set2 = set2.difference(set1)
print(my_set)
print(my_set2)