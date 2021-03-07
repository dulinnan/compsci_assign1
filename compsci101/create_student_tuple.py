def create_student_tuple(student_name_tuple, student_ids_tuple):
    names_ids_list = []
    index = 0
    while index < len(student_name_tuple):
        name_id_list = []
        name_id_list.append(student_name_tuple[index])
        name_id_list.append(student_ids_tuple[index])
        names_ids_list.append(tuple(name_id_list))
        index += 1
    names_ids_tuple = tuple(names_ids_list)
    return names_ids_tuple

if __name__ == "__main__":
    student_name_tuple = ("Peter", "Jane", "Kathy", "Mark")
    student_ids_tuple = (1234, 5678, 91011, 121314)
    student_data_tuple = create_student_tuple(student_name_tuple, student_ids_tuple)
    print(student_data_tuple)