""" Filter - It can filter the items from the list
    based on the logic
     return less number of items """

numbers = [1,2,3,4,5,6,7,8,9,10]
def even(num):
    return num % 2 == 0
def odd(num):
    return num % 2 != 0
even_numbers = filter(even,numbers)
print(list(even_numbers))
odd_numbers = filter(odd,numbers)
print(list(odd_numbers))

# # we can also used to write in one line lambda function
# num = [1,4,7,8,9,11,12,14,17,16,19]
# even_lambda = lambda num: num % 2 == 0
# print(even_lambda)
# odd_lambda = lambda num: num % 2 != 0
# print(odd_lambda)