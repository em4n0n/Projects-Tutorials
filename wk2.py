def read_file(file_name):
    file = open(file_name, 'r')
    data = file.read()
    print(data)
    return data

    file.close()
    raise NotImplementedError()

def read_file_into_list(file_name):
    file = open(file_name, 'r+')
    data = file.readlines()
    print(data)
    return data

    file.close()
    raise NotImplementedError()


def write_first_line_to_file(file_contents, output_filename):
    split_file = file_contents.split('\n') 
    line_first = split_file[0] 

    with open(output_filename, 'w') as file: 
        file.write(line_first) 

    return output_filename 
    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    with open(file_name, 'r') as lines:
        lines = lines.readlines()
        even_list = lines[1::2]

    return even_list
    raise NotImplementedError()

### Function read_file_in_reverse
### Short file test did not pass.
def read_file_in_reverse(file_name):
    f = open(file_name, 'r')
    f_content_list = f.readlines()
    for lines in file_name [::-1]:
        print(lines)
    return f_content_list
    raise NotImplementedError()

def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()

    def read_file_in_reverse(file_name):
    with open(file_name, 'r') as file:   
        data = file.readlines()
    data_reversed = [i for i in data[::-1]]
    
    print(data_reversed)
    return data_reversed