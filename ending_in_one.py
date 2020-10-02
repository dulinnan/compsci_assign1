def print_numbers_ending_in_one(first_num, last_num, step_num):
    index = first_num
    input_numbers = []
    while index <= last_num:
        if (index % 10 == 1):
            input_numbers.append(index)
        index += step_num
    
    for number in range(len(input_numbers)): 
        print(input_numbers[number], end = ' ') 


if __name__ == "__main__":
    print_numbers_ending_in_one(1, 13, 2)
    print_numbers_ending_in_one(1, 121, 3)
    print_numbers_ending_in_one(20, 80, 2)