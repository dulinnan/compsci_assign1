"""Assignment 3 - Testing functions 1 to 6"""

import random

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Function 1 - initialise_list()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def initialise_list():
    pass

    
def test_initialise_list():
    curr_game_move = initialise_list()
    print(curr_game_move)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Function 2 - concatenate_move()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def concatenate_move(existing_moves, new_move):

    return updated_moves

def test_concatenate_move():
    move_list = [1,8,0,1]
    move_list = concatenate_move(move_list, 8)
    print(move_list)
    move_list = concatenate_move(move_list, 7)
    print(move_list)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Function 3 - move_piece()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def move_piece(pos_list, from_position, to_position):
    pass

def test_move_piece():
    position_list = [0,1,1,1,1,2,2,2,2]
    move_piece(position_list, 1, 0)
    print(position_list)
    move_piece(position_list, 8, 1)
    print(position_list)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Function 4 - find_empty_position()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def find_empty_position(pos_list):

    return index_empty

def test_find_empty_position():
    position_list = [0,1,1,1,1,2,2,2,2]
    empty_point = find_empty_position(position_list)
    print(empty_point)
    position_list = [1,1,0,1,1,2,2,2,2]
    empty_point = find_empty_position(position_list)
    print(empty_point)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Function 5 - get_next_move()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def get_next_move():
    valid_response = ["0","1","2","3","4","5","6","7","8","Q","QUIT","EXIT"]
    user_prompt = "Which piece do you want to move (or Q to quit)? "

    return user_input

def test_get_next_move():
    next_move = get_next_move()
    print(next_move)
    next_move = get_next_move()
    print(next_move)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Function 6 - suggest_valid_move()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def suggest_valid_move(pos_list, player):
    suggested_move = "00"

    return suggested_move


def test_suggest_valid_move():
    get_move = suggest_valid_move([1,1,0,1,2,2,1,2,2], 1)
    print(get_move)
    get_move = suggest_valid_move([1,1,0,1,2,2,1,2,2], 2)
    print(get_move)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#Print header lines
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Note that the version of list_valid_moves() below is only a stub for testing.
# DO NOT include this version of list_valid_moves in CodeRunner or in section B of the assignment.
def list_valid_moves(pos_list, player):
    if player == 1:
        pos_options = ["12","32","02"]
    if player == 2:
        pos_options = ["00"]
        pos_options.clear()
    return pos_options


def print_header(number, text):
    number_of_symbols = 30
    number_of_digits = 30
    number_str = str(number)
    if number > 9:
        number_of_digits = 10
        number_str = number_str + " "
    text = "   " + text
    print("-" * number_of_symbols)
    print(number_str * number_of_digits)
    print(text)
    print(number_str * number_of_digits)
    print("-" * number_of_symbols)

def get_menu_selection():
    print()
    print("  1. initialise_list()")
    print("  2. concatenate_move()")
    print("  3. move_piece()")
    print("  4. find_empty_position()")
    print("  5. get_next_move()")
    print("  6. suggest_valid_move()")
    print("  0. Exit")
    user_selection = int(input("    Enter selection (0, 1, 2, 3, 4, 5, or 6): "))
    print()
    return user_selection

def main():
    user_selection = 1
    while user_selection != 0:
        user_selection = get_menu_selection()
        if user_selection == 1:
            print_header(1, "Assignment 3, Function 1 - \n   initialise_list()")
            test_initialise_list()
        elif user_selection == 2:
            print_header(2, "Assignment 3, Function 2 - \n   concatenate_move()")
            test_concatenate_move()
        elif user_selection == 3:
            print_header(3, "Assignment 3, Function 3 - \n   move_piece()")
            test_move_piece()
        elif user_selection == 4:
            print_header(4, "Assignment 3, Function 4 - \n   find_empty_position()")
            test_find_empty_position()
        elif user_selection == 5:
            print_header(5, "Assignment 3, Function 5 - \n   get_next_move()")
            test_get_next_move()
        elif user_selection == 6:
            print_header(6, "Assignment 3, Function 6 - \n   suggest_valid_move()")
            test_suggest_valid_move()
        print("-" * 30)
        print("-" * 30)

main()