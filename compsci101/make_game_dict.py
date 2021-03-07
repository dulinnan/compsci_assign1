def print_dictionary(data_dict):
    key_list = list(data_dict.keys())
    key_list.sort()
    for key in key_list:
        print(key, ": ", data_dict[key], sep="")


def make_game_dict(game_list):
    output = {}
    game_publisher_list = []
    game_name_list = []
    for each_game_tuple in game_list:
        game_publisher = each_game_tuple[0]
        if (game_publisher not in game_publisher_list):
            game_publisher_list.append(game_publisher)
    sorted_game_publisher_list = sorted(game_publisher_list)
    index = 0
    while index < len(sorted_game_publisher_list):
        game_name_list.append([])
        index += 1
    for each_game_tuple in game_list:
        game_publisher = each_game_tuple[0]
        game_name = each_game_tuple[1]
        index_of_game_publisher = sorted_game_publisher_list.index(
            game_publisher)
        game_name_list[index_of_game_publisher].append(game_name)
    new_index = 0
    while new_index < len(sorted_game_publisher_list):
        sorted_game_names = sorted(game_name_list[new_index])
        output[sorted_game_publisher_list[new_index]
               ] = sorted_game_names
        new_index += 1
    return output


if __name__ == "__main__":
    game_list = [("EA", "FIFA 21"),
                 ("Capcom", "Street Fighter 5"),
                 ("EA", "Jedi: Fallen Order"),
                 ("Microsoft", "Forza Horizon 4"),
                 ("Microsoft", "Crackdown 3")
                 ]
    game_dict = make_game_dict(game_list)
    print_dictionary(game_dict)
