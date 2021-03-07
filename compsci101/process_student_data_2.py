def print_dictionary(data_dict):
    key_list = list(data_dict.keys())
    key_list.sort()
    for key in key_list:
        print(key, ": ", data_dict[key], sep="")


def process_student_data(file_name):
    with open(file_name) as f:
        read_name_list = f.readlines()
    f.close()
    sanitised_list = []
    student_names_list = []
    student_grades_list = []
    output = {}
    for every_record in read_name_list:
        sanitised_record = every_record.replace("\n", "").strip()
        sanitised_list.append(sanitised_record)
    for each_record in sanitised_list:
        student_name_string_list = each_record.split(" ")[:-1]
        student_name = " ".join(student_name_string_list)
        if student_name not in student_names_list:
            student_names_list.append(student_name)
    sort_names_list = sorted(student_names_list)
    for index in list(range(len(sort_names_list))):
        student_grades_list.append([])
    index = 0
    while index < len(sort_names_list):
        for each_record in sanitised_list:
            student_name_string_list = each_record.split(" ")[:-1]
            student_name = " ".join(student_name_string_list)
            if (sort_names_list[index] == student_name):
                student_grades_list[index].append(
                    int(each_record.split(" ")[-1]))
                student_grades_list[index].sort()
        index += 1
    index_of_student = 0
    while index_of_student < len(student_grades_list):
        output[sort_names_list[index_of_student]
               ] = tuple(student_grades_list[index_of_student])
        index_of_student += 1
    return output


if __name__ == "__main__":
    file_path = "./input2.txt"
    data_dict = process_student_data(file_path)
    print_dictionary(data_dict)
