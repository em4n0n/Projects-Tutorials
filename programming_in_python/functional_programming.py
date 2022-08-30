import functools

my_list = [1, 2, 3, 4, 5]

def add_it(x, y):
    return (x + y)

sum = functools.reduce(add_it, my_list)

print(sum)