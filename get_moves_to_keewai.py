def get_moves_to_keewai(pos_list, empty_point, player, pos_options):
    if (pos_list[0] == player):
        new_pos_option = str(0) + str(empty_point)
        pos_options.append(new_pos_option)

    else:
        to_check_pos = []

        if empty_point == 1:
            to_check_pos.append(8)
            to_check_pos.append(2)
        elif empty_point == 8:
            to_check_pos.append(7)
            to_check_pos.append(1)
        else:
            to_check_pos.append(empty_point-1)
            to_check_pos.append(empty_point+1)
        if (pos_list[to_check_pos[0]] == player):
            new_pos_option = str(to_check_pos[0]) + str(empty_point)
            pos_options.append(new_pos_option)

        if (pos_list[to_check_pos[1]] == player):
            new_pos_option = str(to_check_pos[1]) + str(empty_point)
            pos_options.append(new_pos_option)

    return pos_options


if __name__ == "__main__":
    pos_list = [2, 0, 1, 1, 1, 2, 2, 2, 1]
    spare_point = 1
    player = 2
    pos_options = ["00"]
    pos_options = get_moves_to_keewai(
        pos_list, spare_point, player, pos_options)
    print(pos_options)
