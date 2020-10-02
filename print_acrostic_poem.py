def print_acrostic_poem(poem_lines_list):
    for word in poem_lines_list:
        first_letter_capitalized = word[0].capitalize()
        print(first_letter_capitalized, " is for ", word)


if __name__ == "__main__":
    acrostic_words_1 = ["terrific", "unbelievable", "interesting"]
    acrostic_words_2 = ["wonderful", "exciting", "king", "adventurous"]
    print_acrostic_poem(acrostic_words_1)
    print_acrostic_poem(acrostic_words_2)