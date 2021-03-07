def get_largest_and_smallest_numbers(filename):
    with open(filename) as f:
        the_list = f.read()
        the_list = the_list.replace("\n", ",").strip()
        the_list = the_list.split(",")
    f.close()

    the_list = list(map(int, the_list))

    min_value = int(min(the_list))
    max_value = int(max(the_list))

    new_list = list()
    new_list.append(min_value)
    new_list.append(max_value)
    the_tuple = tuple(new_list)

    return the_tuple


if __name__ == "__main__":
    file_path = "./Lab07Q05_2.txt"
    print(get_largest_and_smallest_numbers(file_path))
