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

#Add a new item to the original dictionary, and see that the keys list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change the key list gets updated

#values method returns all the values in the dictionary
#Make a change in the original dictionary, and see that the values list gets updated as well:

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change

#Get Items
#The items() method will return each item in a dictionary, as tuples in a list.
print(this_dict.items())

if "model" in this_dict:
  print("Yes, 'model' is one of the keys in the this_dict dictionary")

# changing values
this_dict["year"] = 2018

#The update() method will update the dictionary with the items from the given argument.
#The argument must be a dictionary, or an iterable object with key:value pairs.
this_dict.update({"brand": "BMW"})

# Adding Items
this_dict["city"] = "london"
this_dict.update({"owner": "Miles"})
print(this_dict)

# Removing items
this_dict.pop("model")
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
this_dict.popitem()

# The del keyword removes the item with the specified key name:
that_dict = {
  "Name": "Miles",
  "Age": 10,
  "Race": "Asian"
}

# The clear() method empties the dictionary:
# that_dict.clear()

del that_dict["Race"]
print(that_dict)

# The del keyword can also delete the dictionary completely:
del that_dict

# looping through a dict
for x in this_dict:
  print(this_dict[x])

for k in this_dict.keys():
    print(k)