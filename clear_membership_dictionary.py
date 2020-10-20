def clear_membership_dictionary(member_dict):
    nested_tuple = list(member_dict.items())
    expired_user_id = []
    for each_tuple in nested_tuple:
        listify_tuple = list(each_tuple)
        listify_member_detail = list(listify_tuple[1])
        member_status = listify_member_detail[-1]
        if member_status == False:
            expired_user_id.append(listify_tuple[0])
    for member_id in expired_user_id:
        member_dict.pop(member_id)

if __name__ == "__main__":
    member_dict = {486318: ('Ken', 'USA', 43, 2012, True),
                   194052: ('Dee Jay', 'Spain', 57, 2018, False),
                   147729: ('Fei Long', 'Denmark', 58, 2011, True),
                   188617: ('Akuma', 'Sweden', 60, 2010, True),
                   449009: ('Cammy', 'New Zealand', 35, 2011, True)}
    clear_membership_dictionary(member_dict)
    print(member_dict)
