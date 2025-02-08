
def myFunction(name):
    print(f"value received is {name}")
myFunction("miles")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#You can also send arguments with the key = value syntax.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# To specify that a function can have only positional arguments, add , / after the arguments:
def my_function(x, /):
  print(x)

my_function("miles")

# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function(*, x):
  print(x)

my_function(x = 3)