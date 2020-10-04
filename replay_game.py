def get_perepere_char(perepere_type):
    if perepere_type == 1:
        perepere_char = "O"
    elif perepere_type == 2:
        perepere_char = "X"
    else:
        perepere_char = " "
    return perepere_char


def get_perepere(position, position_list):
    output = "[ ]"
    if 1 <= position < 9:
        perepere_char = get_perepere_char(position_list[position])
        output = perepere_char
    return output


# Also include in the CodeRunner question for replay_game
def draw_papa_taakaro(position_snapshot):
    print(" "*17, "3", sep="")
    print(" "*16, get_perepere(3, position_snapshot), sep="")
    print(" "*9, "2       .       4", sep="")
    print(" "*8, get_perepere(2, position_snapshot), "ˍˍˍˍ./ \.ˍˍˍˍ",
          get_perepere(4, position_snapshot), sep="")
    print(" "*11, "'.         .'", sep="")
    print(" "*6, "1  _.-'    0    '-._  5", sep="")
    print(" "*5, get_perepere(1, position_snapshot), "  '-.   ", get_perepere(0,
                                                                              position_snapshot), "  .-'   ", get_perepere(5, position_snapshot), sep="")
    print(" "*11, ".'         '.", sep="")
    print(" "*9, "8 ˉˉˉˉ'\ /'ˉˉˉˉ 6", sep="")
    print(" "*8, get_perepere(8, position_snapshot), "      '      ",
          get_perepere(6, position_snapshot), sep="")
    print(" "*17, "7", sep="")
    print(" "*16, get_perepere(7, position_snapshot), sep="")


def replay_game(pos_list, move_list):
    draw_papa_taakaro(pos_list)
    empty_position = 0
    player_moving = 1
    print()
    print("Replaying game:")
    print()
    current_empty_point = pos_list.index(0)
    index_of_move_list = 0
    while index_of_move_list < len(move_list):
        if (index_of_move_list % 2) == 0:  # Player 1's move
            pos_list[current_empty_point] = 1
            pos_list[move_list[index_of_move_list]] = 0
            print(">> Player 1 ", pos_list)
            formatted_str = '>> Player 1 moves from %s to %s' % (
                move_list[index_of_move_list], current_empty_point)
            print(formatted_str)
            current_empty_point = move_list[index_of_move_list]
            draw_papa_taakaro(pos_list)

        if (index_of_move_list % 2) != 0:  # Player 2's move
            pos_list[current_empty_point] = 2
            pos_list[move_list[index_of_move_list]] = 0
            print(">> Player 2 ", pos_list)
            formatted_str = '>> Player 2 moves from %s to %s' % (
                move_list[index_of_move_list], current_empty_point)
            print(formatted_str)
            current_empty_point = move_list[index_of_move_list]
            draw_papa_taakaro(pos_list)
        
        while True:
            user_input = input("Press ENTER to continue.")
            if user_input == "":
                break

        index_of_move_list += 1

    print("End of game replay.")


if __name__ == "__main__":
    pos_list = [0, 1, 1, 1, 1, 2, 2, 2, 2]
    move_list = [1, 8, 0, 6]
    replay_game(pos_list, move_list)

