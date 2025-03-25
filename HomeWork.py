import random

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

mutate_list([1,2,3,4,5])

#TODO: 1 print
