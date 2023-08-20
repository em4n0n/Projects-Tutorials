try:
    with open('sample', 'a') as file:
        file.writelines("\nThis is a new file.")
except FileNotFoundError as e:
    print("ERROR", e)