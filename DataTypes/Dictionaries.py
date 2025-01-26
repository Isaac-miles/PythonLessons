#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

this_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# using the dict constructor
my_dict = dict(name = "John", age = 36, country = "Norway")
print(this_dict," and ",my_dict)

# accessing Items
print(this_dict['model'])  #throws an error when an item is not found
print(this_dict.get("models","I didn't see it")) #returns non when an item is not found or an optional value supplied

print(this_dict.keys()) # keys method returns all the keys in the dictionary
print(this_dict.values()) # values method returns all the values in the dictionary

#Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change