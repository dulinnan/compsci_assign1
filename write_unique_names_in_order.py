def write_unique_names_in_order(filename_in, filename_out):
    with open(filename_in) as f:
        read_name_list = f.read()
        read_name_list = read_name_list.replace("\n", ",").strip()
        read_name_list = read_name_list.split(",")
    f.close()
    unique_name_list = []
    [unique_name_list.append(x)
     for x in read_name_list if (x not in unique_name_list and x != "")]
    unique_name_list.sort()
    index = 0
    output = []
    output_file = open(filename_out, "w")
    while index < len(unique_name_list):
        output_str = '%s. %s\n' % (index+1, unique_name_list[index])
        output.append(output_str)
        output_file.write(output_str)
        index += 1
    output_file.close()
    return output[499]


if __name__ == "__main__":
    file_path = "./Lab07Q06.txt"
    output_file_path = "./Lab07Q06_answer.txt"
    print(write_unique_names_in_order(file_path, output_file_path))
