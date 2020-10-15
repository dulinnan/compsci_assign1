def print_dictionary(data_dict):
    key_list = list(data_dict.keys())
    key_list.sort()
    for key in key_list:
        print(key, ": ", data_dict[key], sep="")


def get_word_lengths(file_name):
    with open(file_name) as f:
        read_words_list = f.read()
        read_words_list = read_words_list.replace("\n", ",").strip()
        read_words_list = read_words_list.split(",")
    f.close()
    output = {}
    length_count_list = []
    length_counter_list = []
    for each_word in read_words_list:
        each_word_length = len(each_word)
        if (each_word_length not in length_count_list):
            length_count_list.append(each_word_length)
    sorted_length_count_list = sorted(length_count_list)
    index = 0
    while index < len(sorted_length_count_list):
        length_counter_list.append(0)
        index += 1
    for each_word in read_words_list:
        each_word_length = len(each_word)
        index_of_word_length = length_count_list.index(each_word_length)
        length_counter_list[index_of_word_length] += 1
    new_index = 0
    while new_index < len(sorted_length_count_list):
        output[sorted_length_count_list[new_index]
               ] = length_counter_list[new_index]
        new_index += 1
    return output


if __name__ == "__main__":
    file_name = "./List_Of_Words1.txt"
    word_length_dict = get_word_lengths(file_name)
    print_dictionary(word_length_dict)
