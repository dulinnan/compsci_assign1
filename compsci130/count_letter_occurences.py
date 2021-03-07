def sanitise_list(list_input):
    output = [x for x in list_input if x.isalpha()]
    return output

def print_dictionary(data_dict):
    key_list = list(data_dict.keys())
    key_list.sort()
    for key in key_list:
        print(key, ":", data_dict[key], sep="")

def count_letter_occurences(filename):
    occurences_dict = {}
    with open(filename) as f:
        read_words_list = f.read()
        read_words_list = read_words_list.replace("\n", " ").strip()
        read_words_list = read_words_list.split(" ")
    f.close()
    words_list = sanitise_list(read_words_list)
    for each_word in words_list:
        for letter in each_word:
            new_dict = {}
            # make every letter lower case
            lower_case_letter = letter.lower()
            # check if key exists in dictionary
            if lower_case_letter in occurences_dict.keys():
                # if exists, then we increment the count
                new_dict = {lower_case_letter: occurences_dict.get(lower_case_letter) + 1}   
            else:
                # if not, then we add it to the dict with count=1
                new_dict = {lower_case_letter: 1}
            occurences_dict.update(new_dict)
    print_dictionary(occurences_dict)

if __name__ == "__main__":
    path_to_file = "./file1.txt"
    count_letter_occurences(path_to_file)