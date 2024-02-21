""" Dictionary - dictionaries are used to store data values in key:value pairs
name ="vani" key->name, value->"vani"
A dictionary is an unordered collection of data"""
my_dict = {}
my_dict2 = dict()
print(type(my_dict))
print(type(my_dict2))


phone_book = {"Batman": 987654321, "Superman": 1234567890, "Wonder": 97876545}
print(len(phone_book))
print(phone_book["Batman"])

phone_book2 = dict(Batman=123, Cersei=342, GB=323)
print(phone_book2)
print(phone_book2.get('GB'))
print(phone_book2.get("GB"))

vani_details = dict(name="vani", age=34, isFemale=True, Address="Alkapoor")
kavya_details2 = {"name": "kavya", "90": 34.34, "isFemale": True, "Address": "America"}
print(kavya_details2.get("90"))


my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 95}
print(len(my_dict))
print(my_dict)









