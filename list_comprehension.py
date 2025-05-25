#create a list of squares
from os import access

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

vector = [[1,2,3,4],[5,6,7],[8,9,10]]
#flatten this list
flat = [num for list_item in vector for num in list_item]
# print(flat)

numbers = []
for list_item in vector:
    for num in list_item:
        numbers.append(num)
    # print(numbers)

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
#the following list comprehension will transpose rows and columns:
num_columns = len(matrix[0]) if matrix else 0
transpose_matrix = [[row[i] for row in matrix] for i in range(num_columns)]
# print(transpose_matrix)


transpose_matrix_1 =[]
for i in range(num_columns):
    column = []
    for row in matrix:
        column.append(row[i])
    transpose_matrix_1.append(column)
# print(transpose_matrix_1)

transpose_matrix_1 =[]
for i in range(num_columns):
    transpose_matrix_1.append([row[i] for row in matrix])
# print(transpose_matrix_1)

using_zip = list(zip(*matrix))
print(using_zip)
