def get_two_words(numbers_tuple, words_tuple):
    word_num_dict = dict(zip(words_tuple, numbers_tuple))
    two_greatest_numbers = sorted(word_num_dict)[-2:]
    output = []
    for number in two_greatest_numbers:
        output.append(word_num_dict.get(number))
    output = tuple(output)

    return output


if __name__ == "__main__":
    words = ("mouth", "in", "look", "do", "gift", "a", "the", "horse", "not")
    numbers = (81, 24, 11, 63, 70, 60, 26, 73, 14)
    print(get_two_words(words, numbers))
