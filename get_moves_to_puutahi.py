def get_moves_to_puutahi(pos_list, player, pos_options):
    opposite_player = 2 if player == 1 else 1
    player_index_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = pos_list.index(player, index_pos)
            # Add the index position in list
            player_index_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break

    to_check_pos = []
    checked_pos = []
    for player_index in player_index_list:
        if player_index == 1:
            to_check_pos.append(8)
            to_check_pos.append(2)
        elif player_index == 8:
            to_check_pos.append(7)
            to_check_pos.append(1)
        else:
            to_check_pos.append(player_index-1)
            to_check_pos.append(player_index+1)
        for position in to_check_pos:
            if (pos_list[position] == opposite_player and position not in checked_pos):
                checked_pos.append(position)
                new_pos_options = str(player_index) + str(0)
                pos_options.append(new_pos_options)
    pos_options = list(dict.fromkeys(pos_options))
    return pos_options


if __name__ == "__main__":
    pos_list = [0, 1, 2, 1, 1, 2, 2, 1, 2]
    player = 2
    pos_options = ["00"]
    pos_options = get_moves_to_puutahi(pos_list, player, pos_options)
    print(pos_options)
