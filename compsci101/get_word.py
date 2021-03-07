def get_word(message):
    print(message)
    word = ""
    user_input = input("> ")
    while True:
        if(len(user_input) > 5 and " " not in user_input):
            word = user_input
            break
        else:
            user_input = input("> ")
    return word


if __name__ == "__main__":
    word = get_word("Enter a valid word")
    print("word: ", word)
