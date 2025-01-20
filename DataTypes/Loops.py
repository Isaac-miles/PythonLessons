# While loops
i = 1
while i <=3:
    print("Miles ", i)
    i=i+1

m=1
while m <= 5:
    print("Neon ", end="")
    n=1
    while n <= 3:
        print("Scissors ", end="")
        n = n+1
    m=m+1
    print()


# For loops
listNames = ['Miles','Kelvin','Josiah']

for name in listNames:
    print(name,end=" ")

for i in range(4,16,2):
    print(i)

for x in [0, 1, 2]:
  pass

#Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)