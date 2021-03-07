def sanitise_list(list_input):
    # remove all non-alphanumeric characters from the list
    alphanumeric_only_list = [x for x in list_input if x.isalpha()]
    # convert all strings to lower case
    all_lower_case_list = [word.lower() for word in alphanumeric_only_list]
    # create a dictionary, using the List items as keys.
    # this will automatically remove any duplicates 
    # because dictionaries cannot have duplicate keys.
    duplicates_removed_list = list(dict.fromkeys(all_lower_case_list))
    # sort the list in alphabetical order
    duplicates_removed_list.sort()
    # return the list
    return duplicates_removed_list

def prompt_user_input_for_filename():
    filename = input("Enter filename: ")
    return filename

def handle_read_file(read_lines_list): 
    nested_list = []
    output = []
    for line in read_lines_list:
        read_words_list = line.replace("\n", ",").strip()
        read_words_list = read_words_list.replace(" ", ",").strip()
        read_words_list = read_words_list.split(",")
        nested_list.append(read_words_list)
    while nested_list:
        # bad way of flattening a nested list 
        # because .pop() is O(n)
        # but there is no way to do it in linear time 
        # from a list in Python without extra storage space
        output.extend(nested_list.pop(0))
    return output
    
def count_word_occurances():
    path_to_file = prompt_user_input_for_filename() 
    with open(path_to_file) as f:
        read_words_list = f.readlines()
    f.close()
    words_list = handle_read_file(read_words_list)
    sanitised_list = sanitise_list(words_list)
    print(sanitised_list)


if __name__ == "__main__":
    count_word_occurances()