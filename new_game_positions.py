def new_game_positions(start_index):
    output_list = [0]
    for i in range(8):
        output_list.append(1)
    if (5 <= start_index < 9):
        for i in range(start_index-4, start_index):
            output_list[i] = 2
    if (1 <= start_index < 5):
        for i in range(1, start_index):
            output_list[i] = 2
        for i in range(start_index+4, 9):
            output_list[i] = 2

    return output_list


if __name__ == "__main__":
    new_game = new_game_positions(6)
    print(new_game)
