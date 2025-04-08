import random
from prettytable import PrettyTable
from collections import deque
def add(n,m):
    return n+m

def mutate_list(a_list):
    b_list =[]
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1,3)
        new_item = add(new_item, item)
        b_list.append(new_item)
    print(b_list)

# mutate_list([1,2,3,4,5])
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
# table.add_column("Type",["Electric","Water","Fire"])
# # table.align = "r"
# print(table)

a = [2,4,6,8,9,7,3,11,12]
# a[len(a):] = [a]
a.insert(len(a),5)
a.insert(0,23)
print(a)
print(list.index(a,3,3,9))
print(list.count(a,3))
print(f"append to the end of the list {a}")

queue = deque(["Isaac","Miles","Davies","Humphrey"])
queue.append("Josiah")
print(queue.popleft())
print(queue.pop())

print(type(queue))

print("_"*20)
queue_a = deque(["A","B","C","D","E"])
print(queue_a)
print("rotate to the right")
queue_a.appendleft(queue_a.pop())
print(queue_a)
print("rotate left")
queue_a.append(queue_a.popleft())
print(queue_a)

# def tail(filename, n=10):
#     'Return the last n lines of a file'
#     with open(filename) as f:
#         return deque(f, n)
#
# print(tail("Isaac_Resume",5))