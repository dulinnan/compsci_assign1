def print_dictionary(data_dict):
    key_list = list(data_dict.keys())
    key_list.sort()
    for key in key_list:
        print(key, ": ", data_dict[key], sep="")


def process_word_files(file_name):
    # Using readline()
    file_open = open(file_name, 'r')
    count = 0
    starting_char = ""
    min_length = None
    max_length = None
    words_with_starting_char = []
    length_range = []
    words_list = []

    while True:
        # Get next line from file
        line = file_open.readline()
        count += 1
        # if line is empty
        # end of file is reached
        if not line:
            break
        if count == 1:
            starting_char = line.replace("\n", "").strip()
        if count == 2:
            min_length = int(line)
        if count == 3:
            max_length = int(line)
        if (line.startswith(starting_char)):
            words_with_starting_char.append(line.replace("\n", "").strip())
    file_open.close()
    if (min_length != None and max_length != None):
        length_range = list(range(min_length, max_length+1))
    for word_length in list(range(len(length_range))):
        words_list.append([])
    index_of_length = 0
    while index_of_length < len(length_range):
        for each_word in words_with_starting_char:
            if len(each_word) == length_range[index_of_length]:
                words_list[index_of_length].append(each_word)
                words_list[index_of_length].sort()
        index_of_length += 1
    index = 0
    output = {}
    while index < len(words_list):
        output[length_range[index]] = words_list[index]
        index += 1
    for key, value in output.items():
        if (len(value) == 0 or value == [] or value is None):
            output.pop(key)
    return output


if __name__ == "__main__":
    file_path = "./many_words.txt"
    data_dict = process_word_files(file_path)
    print_dictionary(data_dict)
