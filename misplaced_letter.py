def get_string_without_matches(letters_to_check, letters):
    non_matched_strings = ""
    i = 0
    while i < len(letters):
        if letters[i] != letters_to_check[i]:
            non_matched_strings += letters_to_check[i]
        else:
            non_matched_strings += " "
        i += 1
    return non_matched_strings


def get_number_correct_not_in_place(hidden_letters, user_letters):
    counter = 0
    non_matching_hidden_letters = get_string_without_matches(
        hidden_letters, user_letters)
    non_repetitive_user_letters = ""
    non_repetitive_non_matching_hidden_letters = ""
    iterated_letter_user = ""
    iterated_letter_hidden = ""
    for letter in user_letters:  # remove duplicates and replace with space
        if iterated_letter_user.find(letter) == -1:
            iterated_letter_user += letter
            non_repetitive_user_letters += letter
        else:
            non_repetitive_user_letters += " "
    for letter in non_matching_hidden_letters:  # remove duplicates and replace with space
        if iterated_letter_hidden.find(letter) == -1:
            iterated_letter_hidden += letter
            non_repetitive_non_matching_hidden_letters += letter
        else:
            non_repetitive_non_matching_hidden_letters += " "
    i = 0
    while i < len(non_repetitive_user_letters):
        j = 0
        while j < len(non_repetitive_non_matching_hidden_letters):
            if (non_repetitive_user_letters[i] == non_repetitive_non_matching_hidden_letters[j] and i != j and non_repetitive_user_letters[i] != " "):
                counter += 1
            j += 1
        i += 1
    return counter


if __name__ == "__main__":
    print(get_number_correct_not_in_place("CACC", "CACC"))
    print(get_number_correct_not_in_place("AACC", "CABA"))
    print(get_number_correct_not_in_place("BABC", "BBDB"))
    print(get_number_correct_not_in_place("ABCD", "DDBA"))
    # print(get_string_without_matches("AACC", "CABA"))
