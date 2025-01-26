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