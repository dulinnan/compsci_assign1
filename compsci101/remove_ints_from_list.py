def remove_ints_from_list(data_list):
    to_remove_item_list = []
    for item in data_list:
        if (str(item).isdigit() ):
            to_remove_item_list.append(item)
    for to_remove_item in to_remove_item_list:
        data_list.remove(to_remove_item)


if __name__ == "__main__":
    data_list = [1, "hello", 2, 3, "world"]
    # data_list = [5, 4, 3, 2, 1]
    remove_ints_from_list(data_list)
    print(data_list)
