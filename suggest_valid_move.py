from random import *

def suggest_valid_move(pos_list, player):
    output = "00"
    randomised_list_of_strings = list_valid_moves(pos_list, player)
    if (len(randomised_list_of_strings) == 0 or randomised_list_of_strings == None):
        return output
    else:
        shuffle(randomised_list_of_strings)
        return (randomised_list_of_strings[0])


if __name__ == "__main__":
    get_move = suggest_valid_move([1, 1, 0, 1, 2, 2, 1, 2, 2], 2)
    print(get_move)
