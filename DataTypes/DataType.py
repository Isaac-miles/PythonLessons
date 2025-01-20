
the_list = ["apple", "banana", "cherry", "apple", "cherry"]
#list method
the_list.append("orange")
print(the_list)
print(len(the_list))

#using list constructor
this_list = list(("apple", "banana", "cherry","Melon")) # note the double round-brackets
print(this_list[1:3])
this_list.remove("banana")

th_list = ["apple", "banana", "cherry"]
if "apple" in th_list:
  print("Yes, 'apple' is in the fruits list")

tha_list = ["apple", "banana", "cherry"]
for x in tha_list:
  print(x)

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# [expression for item in iterable if condition == True]
new_list = [x for x in fruits if "a" in x]
print(new_list)

new_list_ = [x for x in fruits]
new__list = [x if x != "banana" else "orange" for x in fruits]
print(new__list)