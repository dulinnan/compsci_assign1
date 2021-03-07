def print_first_difference(string1, string2):
    zipped_strings = zip(string1, string2)
    for index, tup in enumerate(zipped_strings):
        if tup[0] != tup[1]:
            print("Strings differ at position " + str(index+1))
            break
    else:
        if len(zipped_strings) != len(max(string1, string2)):
            print("Strings differ at position " + str(len(min(string1, string2))+1))
        else:
            print("Strings are identical")


if __name__ == "__main__":
    print_first_difference("abcdef", "abcdef")