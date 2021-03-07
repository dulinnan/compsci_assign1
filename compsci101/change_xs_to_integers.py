def change_xs_to_integers(words_list, numbers_list):
    index = 0
    index_max = len(words_list) - 1
    while index < index_max:
        if words_list[index] == "x":
            words_list[index] = numbers_list[-1]
            numbers_list.pop(-1)
        index += 1


if __name__ == "__main__":
    # words_list = ["Some", "x", "can", "go", "x", "the", "x", "square"]
    # numbers_list = [4, 2, 1]
    words_list = ["You", "x", "hunger", "x", "change"]
    numbers_list = [4, 2]
    print(words_list)
    print(numbers_list)
    change_xs_to_integers(words_list, numbers_list)
    print(words_list)
    print(numbers_list)
