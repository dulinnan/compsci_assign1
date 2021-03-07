def main():
    list_1 = [2, 4, 6]
    list_2 = list_1
    dp_something2(list_1, list_2)
    print("list_1", list_1)
    print("list_2", list_2)
    a_list = ["False", 2, "T", '100']
    a_dict = {"better": 3, "days": "True"}
    object_1 = a_list.pop(2) == a_dict["days"][0]
    object_2 = (len(a_list[0])-1) * a_dict["better"]
    object_3 = [int(a_list[2]) / a_list[1]]
    print(type(object_1))
    print(type(object_2))
    print(type(object_3))

def dp_something2(list1, list2):
    for index in range(len(list1)):
        list2[index] = list1[index]/2


main()
