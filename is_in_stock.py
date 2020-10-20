def is_in_stock(inventory_dict, branch, name):
    is_in_stock = False
    inventory_list = inventory_dict.get(branch)
    for each_tuple in inventory_list:
        listify_tuple = list(each_tuple)
        if (listify_tuple[0] == name and listify_tuple[1] > 0):
            is_in_stock = True
    return is_in_stock


if __name__ == "__main__":
    # data_dict = {'New Lynn': [('Gears of War 5', 1), ('Wasteland 3', 3), ('Ghost of Tsushima', 0)],
    #              'Avondale': [('Gears of War 5', 5), ('Wasteland 3', 2), ('Ghost of Tsushima', 1)],
    #              'St. Lukes': [('Gears of War 5', 1), ('Wasteland 3', 1), ('Ghost of Tsushima', 1)]}
    # print(is_in_stock(data_dict, "New Lynn", "Ghost of Tsushima"))
    # print(is_in_stock(data_dict, "Avondale", "Wasteland 3"))
    data_dict = {'New Lynn': [('Gears of War 5', 4), ('Wasteland 3', 0), ('Ghost of Tsushima', 2),
                              ('Forza Horizon 4', 0), ('The Outer Worlds', 0), ('Doom Eternal', 3)],
                 'Avondale': [('Gears of War 5', 3), ('Wasteland 3', 5), ('Ghost of Tsushima', 0),
                              ('Forza Horizon 4', 0), ('The Outer Worlds', 3), ('Doom Eternal', 4)],
                 'St. Lukes': [('Gears of War 5', 4), ('Wasteland 3', 4), ('Ghost of Tsushima', 5),
                               ('Forza Horizon 4', 4), ('The Outer Worlds', 0), ('Doom Eternal', 2)]}
    print(is_in_stock(data_dict, "St. Lukes", "The Outer Worlds"))
    print(is_in_stock(data_dict, "Avondale", "Forza Horizon 4"))
    print(is_in_stock(data_dict, "New Lynn", "Doom Eternal"))
