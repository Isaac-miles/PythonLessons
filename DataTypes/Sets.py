# Sets are unordered datatypes and hence can not be accessed using indexing
my_set = {"apple", "banana", "cherry"}

for x in my_set:
  print(x)

print("apple" in my_set)
print("mango" not in my_set)

# adding Items to a set
my_set.add("mango")

# To add items from another set into the current set, use the update() method.
tropical = {"pineapple", "orange", "papaya"}
my_set.update(tropical)
print("After updating with another set",my_set)

my_list = ["Miles","Josiah","Blessing"]
my_set.update(my_list)
print(my_set)

# Removing Items
my_set.remove("Blessing")
my_set.discard("Miles")
print(my_set)

# removing random Items
my_set.pop()
# clear set
my_set.clear()