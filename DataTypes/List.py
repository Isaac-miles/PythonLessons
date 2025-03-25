
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

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.sort(key = str.lower)

# [expression for item in iterable if condition == True]
new_list = [x for x in fruits if "a" in x]
print(new_list)

new_list_ = [x for x in fruits]
new__list = [x if x != "banana" else "orange" for x in fruits]
print(new__list)

sort_Fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
sort_Fruits.sort(reverse = True)
print(sort_Fruits)

import math

# Fixed values
C = 50
H = 30

# Taking input from the user
D_values = input("Enter comma-separated values for D: ").split(",")

# Print D_values to see its structure
print("D_values after splitting:", D_values)

# Initialize an empty list for results
Q_values = []

# Loop through each D, compute Q, and store in the list
for D in D_values:
    D_int = int(D)  # Convert string to integer
    Q = int(math.sqrt((2 * C * D_int) / H))  # Compute Q
    Q_values.append(str(Q))  # Store result as string

# Print the final result as a comma-separated string
print(",".join(Q_values))
