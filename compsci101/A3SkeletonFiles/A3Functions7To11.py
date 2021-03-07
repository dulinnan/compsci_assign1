"""Assignment 3 - Testing functions 7 to 11"""

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Function 7 - new_game_positions()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def new_game_positions(start_index):
    new_pos = [0]

    return new_pos


def test_new_game_positions():
    new_game = new_game_positions(1)
    print(new_game)
    new_game = new_game_positions(5)
    print(new_game)
    new_game = new_game_positions(7)
    print(new_game)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Function 8 - get_perepere()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def get_perepere(position,position_list):

    return print_string

def test_get_perepere():
    position_list = [0,1,1,1,1,2,2,2,2]
    print(get_perepere(0,position_list))
    print(get_perepere(1,position_list))
    print(get_perepere(5,position_list))


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Function 9 - replay_game()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def replay_game(pos_list, move_list):
    draw_papa_taakaro(pos_list)
    empty_position = 0
    player_moving = 1
    print()
    print("Replaying game:")
    print()


    print("End of game replay.")


def test_replay_game():
    pos_list = [0,1,1,1,1,2,2,2,2]
    move_list = [1,8]
    replay_game(pos_list, move_list)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Function 10 - get_moves_to_keewai()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def get_moves_to_keewai(pos_list, empty_point, player, pos_options):

    return pos_options


def test_get_moves_to_keewai():
    pos_list = [2,0,1,1,1,2,2,2,1]
    spare_point = 1
    player = 1
    pos_options = ["00"]
    pos_options = get_moves_to_keewai(pos_list, spare_point, player, pos_options)
    print(pos_options)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Function 11 - get_moves_to_puutahi()
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def get_moves_to_puutahi(pos_list, player, pos_options):

    return pos_options


def test_get_moves_to_puutahi():
    pos_list = [0,1,1,1,1,2,2,2,2]
    player = 1
    pos_options = ["00"]
    pos_options = get_moves_to_puutahi(pos_list, player, pos_options)
    print(pos_options)








#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#Print header lines
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def get_perepere_char(perepere_type):
    if perepere_type == 1:
        perepere_char = "֍" # Player 1 (computer)
    elif perepere_type == 2:
        perepere_char = "ߋ" # Player 2 (user)
    else:
        perepere_char = " " # Empty position
    return perepere_char


def draw_papa_taakaro(position_snapshot): # Also include in the CodeRunner question for replay_game
    print(" "*17,"3",sep="")
    print(" "*16,get_perepere(3,position_snapshot),sep="")
    print(" "*9,"2       .       4",sep="")
    print(" "*8,get_perepere(2,position_snapshot),"ˍˍˍˍ./ \.ˍˍˍˍ",get_perepere(4,position_snapshot),sep="")
    print(" "*11,"'.         .'",sep="")
    print(" "*6,"1  _.-'    0    '-._  5",sep="")
    print(" "*5,get_perepere(1,position_snapshot),"  '-.   ",get_perepere(0,position_snapshot),"  .-'   ",get_perepere(5,position_snapshot),sep="")
    print(" "*11,".'         '.",sep="")
    print(" "*9,"8 ˉˉˉˉ'\ /'ˉˉˉˉ 6",sep="")
    print(" "*8,get_perepere(8,position_snapshot),"      '      ",get_perepere(6,position_snapshot),sep="")
    print(" "*17,"7",sep="")
    print(" "*16,get_perepere(7,position_snapshot),sep="")

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
    print("  1. new_game_positions()")
    print("  2. get_perepere()")
    print("  3. replay_game()")
    print("  4. get_moves_to_keewai()")
    print("  5. get_moves_to_puutahi()")
    print("  0. Exit")
    user_selection = int(input("    Enter selection (0, 1, 2, 3, 4 or 5): "))
    print()
    return user_selection

def main():
    user_selection = 1
    while user_selection != 0:
        user_selection = get_menu_selection()
        if user_selection == 1:
            print_header(1, "Assignment 3, Function 7 - \n   new_game_positions()")
            test_new_game_positions()
        elif user_selection == 2:
            print_header(2, "Assignment 3, Function 8 - \n   get_perepere()")
            test_get_perepere()
        elif user_selection == 3:
            print_header(3, "Assignment 3, Function 9 - \n   replay_game()")
            test_replay_game()
        elif user_selection == 4:
            print_header(4, "Assignment 3, Function 10 - \n   get_moves_to_keewai()")
            test_get_moves_to_keewai()
        elif user_selection == 5:
            print_header(5, "Assignment 3, Function 11 - \n   get_moves_to_puutahi()")
            test_get_moves_to_puutahi()
        print("-" * 30)
        print("-" * 30)

main()