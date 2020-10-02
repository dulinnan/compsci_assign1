def remove_words_pop(sentence_list, start_position, end_position):
    sentence_list = list(sentence_list)
    number_of_words = len(sentence_list)
    pointer_start = 0
    pointer_end = number_of_words - 1
    while pointer_end >= end_position:
        sentence_list.pop(pointer_end)
        pointer_end -= 1
    while pointer_start < (start_position - 1):
        sentence_list.pop(0)
        pointer_start += 1
    return sentence_list


if __name__ == "__main__":
    sentence_list = "Broccoli is something I love to hate".split()
    sentence_list = remove_words_pop(sentence_list, 2, 5)
    print(sentence_list)
