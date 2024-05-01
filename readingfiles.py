with open("filex.txt", 'r') as file:
    data = file.readlines()

print(len(data))

for i in data:
    print(data)