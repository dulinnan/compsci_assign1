def stores_with_stock(inventory_dict, item):
    output = []
    nested_tuple = list(inventory_dict.items())
    nested_dict = {}
    for each_tuple in nested_tuple:
        each_list = list(each_tuple)
        stock_level_dict = dict(each_list[1])
        nested_dict[each_list[0]] = stock_level_dict
    for store_name, store_stock in nested_dict.items():
        for movie_name, movie_stock in store_stock.items():
            if (movie_name == item and movie_stock > 0):
                output.append(store_name)
    sorted_output = sorted(output)
    return tuple(sorted_output)


if __name__ == "__main__":
    data_dict = {'CBD': [('The Last of Us 2', 3), ('Xenoblade Chronicles', 1),
                         ('Ori and the Will of the Wisps', 5), ('Control', 0)],
                 'Henderson': [('The Last of Us 2', 3), ('Xenoblade Chronicles', 5),
                               ('Ori and the Will of the Wisps', 1), ('Control', 4)],
                 'Manukau City': [('The Last of Us 2', 5), ('Xenoblade Chronicles', 0),
                                  ('Ori and the Will of the Wisps', 5), ('Control', 3)]}
    item = "Xenoblade Chronicles"
    print("Stores with '", item, "': ",
          stores_with_stock(data_dict, item), sep="")
    item = "Control"
    print("Stores with '", item, "': ",
          stores_with_stock(data_dict, item), sep="")
    item = "Doom Eternal"
    print("Stores with '", item, "': ",
          stores_with_stock(data_dict, item), sep="")
