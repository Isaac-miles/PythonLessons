my_tuple = ("apple", "banana", "cherry")
print(len(my_tuple))

this_tuple = ("apple",)
print(type(this_tuple))

the_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(the_tuple[2:5])
print(the_tuple[-4:-1])

th_tuple = ("apple", "banana", "cherry")
if "apple" in th_tuple:
  print("Yes, 'apple' is in the fruits tuple")

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)