def is_odd(number):
    return False if (number % 2 == 0) else True

def extract_middlle_letter(word):
    middle_letter = ""
    word_lenth = len(word)
    if (is_odd(word_lenth)):
        middle_letter = word[int((word_lenth-1)/2)]
    else:
        middle_letter = word[int((word_lenth/2)-1)]
    return middle_letter

def print_dictionary(data_dict):
    key_list = list(data_dict.keys())
    key_list.sort()
    for key in key_list:
        print(key, " ", data_dict[key], sep="")

def get_middle_letter_dictionary(sentence):
    output = {}
    words_list = sentence.split(" ")
    all_lower_case_list = [word.lower() for word in words_list]
    for each_word in all_lower_case_list:
        new_dict = {}
        middle_letter_of_a_word = extract_middlle_letter(each_word)
        new_value = []
        if middle_letter_of_a_word in output.keys():
            new_value = list(output.get(middle_letter_of_a_word))
            new_value.append(each_word)
            duplicates_removed_list = list(dict.fromkeys(new_value))
            new_dict = {middle_letter_of_a_word: duplicates_removed_list}
        else:
            new_value.append(each_word)
            new_dict ={middle_letter_of_a_word: new_value}
        output.update(new_dict)
    return output



if __name__ == "__main__":
    sentence = "Summer is over and the hot days are gone"
    get_middle_letter_dictionary(sentence)