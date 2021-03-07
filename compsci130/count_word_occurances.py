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

def count_word_occurances():
    path_to_file = prompt_user_input_for_filename()
    with open(path_to_file) as f:
        read_words_list = f.read()
        read_words_list = read_words_list.replace("\n", " ").strip()
        read_words_list = read_words_list.split(" ")
    f.close()
    sanitised_list = sanitise_list(read_words_list)
    print(sanitised_list)


if __name__ == "__main__":
    count_word_occurances()