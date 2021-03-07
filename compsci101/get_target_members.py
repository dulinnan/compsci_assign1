def get_target_members(input_dict, country_list, min_age, max_age):
    nested_tuple = list(input_dict.items())
    nested_list = []
    for each_tuple in nested_tuple:
        each_list = []
        listify_tuple = list(each_tuple)
        each_list.append(listify_tuple[0])
        each_list.append(list(listify_tuple[1]))
        nested_list.append(each_list)
    nested_list.sort(key=lambda x: x[1][0])
    return [
        tuple([each_list[1][0], each_list[0]]) for each_list in nested_list if (each_list[1][4] == True and each_list[1][1] in country_list and min_age <= each_list[1][2] <= max_age)]


if __name__ == "__main__":
    member_dict = {486318: ('Ken', 'USA', 43, 2012, True),
                   194052: ('Dee Jay', 'Spain', 57, 2018, False),
                   147729: ('Fei Long', 'Denmark', 58, 2011, True),
                   188617: ('Akuma', 'Sweden', 60, 2010, True),
                   449009: ('Cammy', 'New Zealand', 35, 2011, True)}
    country_list = ['Spain', 'Denmark', 'Sweden']
    target_list = get_target_members(member_dict, country_list, 50, 60)
    print(target_list)
