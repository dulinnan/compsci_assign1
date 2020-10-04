import random
import time     #<<--- This hasn't been taught. Look on Python.org

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Add your 11 functions from
# Section A of Assignment 3
# below:
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>







#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#DO NOT CHANGE ANYTHING BELOW THIS LINE
#DO NOT CHANGE ANYTHING BELOW THIS LINE
# main part of the program
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# The following function redraws the game board (papa tākaro).
def draw_papa_taakaro(position_snapshot):
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

def get_perepere_char(perepere_type):
    if perepere_type == 1:
        perepere_char = "֍" # Player 1 (computer)
    elif perepere_type == 2:
        perepere_char = "ߋ" # Player 2 (user)
    else:
        perepere_char = " " # Empty position
    return perepere_char

def get_play_response(allow_replay):
    if allow_replay == True:
        user_response = input("Play again (Y or N or R for replay)?:").upper()
    else:
        user_response = input("Play again (Y or N)?:").upper()
    if user_response == "Y" or user_response == "YES":
        return_val = "Y"
    elif user_response == "R":
        if allow_replay == True:
            return_val = "R"
        else:
            return_val = ""
    else:
        return_val = ""
    return return_val

def list_valid_moves(pos_list, player):
    pos_options = initialise_list() # First digit is from position; second digit is to position.
    if pos_list[0] == 0:
        # The pūtahi is empty. Look to see if player can move there.
        pos_options = get_moves_to_puutahi(pos_list,player,pos_options)
    else:
        # The pūtahi is full. Look to see if any of the player's pieces can move to the spare point.
        spare_point = find_empty_position(pos_list)
        pos_options = get_moves_to_keewai(pos_list,spare_point,player,pos_options)
    return pos_options

def main():
    print(" "*25,"-----Mū Tōrere-----",sep="")
    print("Instructions:")
    print("The aim of the game is to move your perepere (play pieces) into a configuration \nthat blocks your opponent from moving.")
    print("Each player has four perepere. Player 1 (Computer) is ",get_perepere_char(1)," and Player 2 is ",get_perepere_char(2),".",sep="") 
    print("There are nine positions on the board. The the pūtahi (position 0) is in the \ncentre of the board. This is surrounded by eight kēwai positions (1-8).")
    print("- You may move to an empty connected position. You cannot jump another perepere.")
    print("- If you are in a kēwai position (1-8), you can move to an adjacent number in \nthat range if it is unoccupied. (Note that 1 and 8 are adjacent.)")
    print("- If you are in a kēwai position (1-8) and the flanking kēwai DO NOT BOTH \ncontain perepere from your team, you can move to the pūtahi (position 0) \nif it is unoccupied.")
    print("- If you are in the pūtahi position (0), you can move to a kēwai position \n(1-8) if it is empty.")
    print()
    
    play_game = True
    comp_begin_move = 0
    comp_end_move = 0
    position_init = new_game_positions(random.randint(1,8)) # Initial positions on the board
    position_list = position_init.copy() # Working version of current positions on the board
    curr_game_move = initialise_list()
    while play_game == True:
        comp_move = suggest_valid_move(position_list,1)
        if comp_move == "00":
            print()
            print("You win! Ka rawe!")
            user_choice = get_play_response(True)
            if user_choice == "Y":
                play_game = True
            elif user_choice == "R":
                replay_game(position_init, curr_game_move)
                user_choice = get_play_response(False)
                if user_choice == "Y":
                    play_game = True
                else:
                    play_game = False
            else:
                play_game = False
    
            position_init = new_game_positions(random.randint(1,8))
            position_list = position_init.copy()
            curr_game_move = initialise_list()
        else:
            curr_game_move = concatenate_move(curr_game_move,int(comp_move[0]))
            move_piece(position_list, int(comp_move[0]), int(comp_move[1]))
            print()
            print("Player 1 move:",comp_move[0],"to",comp_move[1])
            print()
            draw_papa_taakaro(position_list)
            pos_options = list_valid_moves(position_list,2)
            if pos_options == []:
                print()
                print("Your opponent wins. Kia kaha!")
                user_choice = get_play_response(True)
                if user_choice == "Y":
                    play_game = True
                elif user_choice == "R":
                    replay_game(position_init, curr_game_move)
                    user_choice = get_play_response(False)
                    if user_choice == "Y":
                        play_game = True
                    else:
                        play_game = False
                else:
                    play_game = False
    
                position_init = new_game_positions(random.randint(1,8))
                position_list = position_init.copy()
                curr_game_move = initialise_list()
            else:
                valid_move = False
                while valid_move != True:
                    print()
                    user_begin_move = get_next_move()
                    print()
                    if user_begin_move.isnumeric() == True:
                        user_begin_move = int(user_begin_move)
                        for check_valid in pos_options:
                            if int(check_valid[0]) == user_begin_move:
                                valid_move = True
                                move_piece(position_list, user_begin_move, int(check_valid[1]))
                                curr_game_move = concatenate_move(curr_game_move, user_begin_move)
                        if valid_move == False:
                            print("Invalid move! Kia tūpato!")
                    else:
                        valid_move = True
                        play_game = False
                if isinstance(user_begin_move, int) == True:
                    draw_papa_taakaro(position_list)
                    time.sleep(3)   #<<--- This hasn't been taught. Look on Python.org
    print("Until next time! Mā te wā!")

main()