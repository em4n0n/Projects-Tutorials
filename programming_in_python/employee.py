import json  # Step 2
from employee import details, employee_name, age, title  # Step 3

def create_dict():  # Step 4
    employee_dict = {  # 4.1
        "first_name": employee_name,
        "age": age,
        "title": title,
    }
    return employee_dict

def write_json_to_file(output_file):  # Step 6
    newfile = open(output_file, "w")  # 6.1
    newfile.write(json_object)  # 6.2
    newfile.close()  # 6.3

# Step 7
write_json_to_file("output.json")