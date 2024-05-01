# def read_file_in_reverse(file_name):

# mylist = [1, 2, 3, 4, 5, 6]

# list2 = []

# for i in range(1, len(mylist) +1):
#     list2.append(mylist[-i])

# print(list2)

#     list2 = mylist[::-1]
#     print(list2)
# print("mylist before reverse:", mylist)
# mylist.reverse()
# print("mylist after reverse", mylist)
# print(mylist)

with open('file.txt', 'r') as file:
    lines = file.readlines()
    items = []
    for line in lines:
        items.append(line)
        items.reverse()

print(items)

