def get_rearranged_list(numbers, index, how_many):
    output = []
    if (how_many == 0):
        output = numbers
    else:
        if (index == 0):
            part_1 = numbers[0: how_many]
            part_2 = numbers[how_many:]
            # print("part_1", part_1)
            # print("part_2", part_2)
            output = part_2 + part_1
        else:
            part_1 = numbers[0: index]
            part_2 = numbers[index: index+how_many]
            part_3 = numbers[index+how_many:]
            # print("part_1", part_1)
            # print("part_2", part_2)
            # print("part_3", part_3)
            output = part_1 + part_3 + part_2
    return output


if __name__ == "__main__":
    numbers = [4, 5, 1, 8, 2]
    # numbers = [2, 3, 4, 5, 6, 7, 8]
    result = get_rearranged_list(numbers, 0, 2)
    print(numbers, "--->", result)
