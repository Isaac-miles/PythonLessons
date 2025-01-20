
the_list = ["apple", "banana", "cherry", "apple", "cherry"]
print(the_list)
print(len(the_list))

#using list constructor
this_list = list(("apple", "banana", "cherry","Melon")) # note the double round-brackets
print(this_list[1:3])

th_list = ["apple", "banana", "cherry"]
if "apple" in th_list:
  print("Yes, 'apple' is in the fruits list")