#1
# my_list = [1, 2, 3]

# def add_to_list(item):
#     return my_list.append(item)


# add_to_list(4)

# print(my_list)

#2
my_list = [1, 2, 3]

def add_to_list(item):
    my_list.append(item)
    return my_list


new_list = add_to_list(4)

print(my_list)
print(new_list)










#3
# my_list = [1, 2, 3]

# def add_to_list(lst, item):
#     nl = lst.copy()
#     nl.append(item)
#     return nl

# new_list = add_to_list(my_list, "bro")

# print(my_list)
# print(new_list)