def compare(text1, text2):
    index = 0                            # initialise an index
    amount_of_common_letter = 0          # initilise a counter
    while index < len(text1):            # loop through every letter of text1
        if text1[index] == text2[index]: # comparing every index-th letter of these two strings
            amount_of_common_letter += 1 # we add increment to the counter
        index += 1                       # we add increment to the index
    return amount_of_common_letter       # we return the counter

if __name__ == "__main__":
    print(compare("Taupo", "Tuatara"))