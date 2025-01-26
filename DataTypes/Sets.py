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

"""
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""

# The union() method returns a new set from both set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
# you can use the | operator in place of union()
set4 = set3 | set2
print(set4)

set5 = set1.union(set2,set3,set4)
print("All sets",set5)

# update method does not return a new set instead changes the original set
set1.update(set5)
print(set1)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
setA = {"apple", "banana", "cherry"}
setB = {"google", "microsoft", "apple"}

setC = setA.intersection(setB)
print(setC)

# you can use the & operator instead of intersect()
setC = setA & setB

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
setA.intersection_update(setB)

# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
setD = {"apple", 1,  "banana", 0, "cherry"}
setE = {False, "google", 1, "apple", 2, True}

setF = setD.intersection(setE)

print(setF)

#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
setH = setE.difference(setD)

#You can use the - operator instead of the difference() method, and you will get the same result.
setH1 = setE - setD

# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.
