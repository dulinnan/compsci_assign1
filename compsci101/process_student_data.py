def process_student_data(filename):
    with open(filename) as f:
        read_name_list = f.readlines()
    f.close()
    sanitised_list = []
    for every_record in read_name_list:
        sanitised_record = every_record.replace("\n", "").strip()
        sanitised_list.append(sanitised_record)
    for every_record in sanitised_list:
        every_record = every_record.split(",")
        student_name = every_record[0]
        student_record = every_record[1:]
        output_str = '%s: %s' % (student_name, student_record)
        print(output_str)


if __name__ == "__main__":
    # file_path = "./student_data_1.txt"
    file_path = "./student_data_2.txt"
    process_student_data(file_path)
