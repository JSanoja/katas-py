"""
Build Tower
Build a pyramid-shaped tower, as an array/list of strings, 
given a positive integer number of floors. 
A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:
"""
def tower_builder(n_floors):
    arr = []
    current = 1
    for i in range(n_floors):        
        space = n_floors - i - 1
        arr.append(space*" " + "*"*current + space*" ")
        current += 2
    return arr
print(tower_builder(5))
