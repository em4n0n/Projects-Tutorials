try:
    with open('sample/filex.txt', 'a') as file:
        file.writelines(["\nThis is a new file created!2", "\nThis is another lines to be created"])
except FileNotFoundError as e:
    print("ERROR", e)

try:
    with open('sample', 'a') as file:
        file.writelines("\nThis is a new file.")
except FileNotFoundError as e:
    print("ERROR", e)