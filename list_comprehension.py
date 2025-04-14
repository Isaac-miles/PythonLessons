#create a list of squares
squares = []
for x in range(10):
    squares.append(x**2)
# print(squares)

#creating this without any side effects
squares_1 = [x**2 for x in range(10)]
# print(squares_1)
#using lambda
square_2 = list(map(lambda a:a**2, range(10)))
# print(square_2)

#listcomp combines the element of two list if they are not equal
comb_list = [(x,y) for x in [1,2,3] for y in [4,5,6] if x!=y]
# print(comb_list)

#this is equivalent to
comb_list_1 = []
for x in [1,2,3]:
    for y in [4,5,6]:
        if x !=y:
            comb_list_1.append((x,y))
# print(comb_list_1)

vec = [[1,2,3,4],[5,6,7],[8,9,10]]
#flatten this list
flat = [num for elem in vec for num in elem]
# print(flat)

for num in vec:
    for el in num:
        print(el)