# List - collection of items which is mutable meaning change or modify in list items
my_list = [1,2,3,4,5]
my_list[1]= 9
print(my_list)
print(type(my_list))

# Tuple - collection of items which is immutable meaning cant change or modify items
my_tuple = (2,4,5,6,7)
# my_tuple[0] = 21   # TypeError : 'tuple'
print(my_tuple)
print(len(my_tuple))
print(type(my_tuple))

# convert list to tuple
new_tup = tuple(my_list)
print(new_tup)

#convert tuple to list
new_list = list(my_tuple)
print(new_list)

