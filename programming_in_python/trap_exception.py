# Starter code
items = [1, 2, 3, 4, 5]
item = items[6]
print(item)

try:
    item = items[6]
    print(item)
except:
    print("Item does not exist in the list.")