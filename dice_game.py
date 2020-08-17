import random

ROUNDS_NUMBER = 3
ACCUMULATED_NUMBER = 0
GOAL_NUMBER = 20
HEADER_STAR_NUMBER = 42
FOOTER_STAR_NUMBER = 16


def random_num_generator(size_of_list):
    """generates a list of random dice numbers, given the size of the list

    Args:
        size_of_list (integer): any integer that is greater or equal to 1

    Example:
        if the size_of_list = 8, then the expected output is something like
        [1, 4, 5, 2, 6, 2, 2, 3]

    Returns:
        list: a list that contains random dice numbers
    """
    random_number_list = []
    index = 1
    while index <= size_of_list:
        random_number = random.randrange(1, 7, 1)
        random_number_list.append(random_number)
        index += 1
    return random_number_list


def list_extractor(input_list, tens_digit_position, units_digit_position):
    """extracts the number from a list given two postion index,
       and combines two numbers as tens and units digit.

    Args:
        input_list (list): a list of random dice numbers more than one item)
        tens_digit_position (integer): postion index of the tens digit
        units_digit_position (integer): postion index of the units digit

    Example: if input_list = [1, 4, 5, 3, 2]
             tens_digit_position = 2, and units_digit_position = 2
             then the expected output is 44.

    Returns: 
        integer: a combined number with a tens and a units digit
    """
    tens_digit = input_list[tens_digit_position - 1] * 10
    units_digit = input_list[units_digit_position - 1] * 1
    add_subtract_num = tens_digit + units_digit
    return add_subtract_num


def user_input_handler():
    """handles user input.

    Expected input: *** on a single line ***
                    either "+"or "-"followed by the position number 
                    (1, 2, 3, 4 or 5) of the tens digit, 
                    followed by a space and finally the position 
                    number (1, 2, 3, 4 or 5) of the units digit.

    Example: if the user input is like "+ 2 1"
             then the expected output is ["+", "2", "1"]

    Returns:
        list: a user input list that contains a plus-minus sign,
              a string that indicates the postion of the tens digit,
              and a string indicates the postion of the units digit.
    """
    user_input = input("  Add/Subtract tens units: ")
    user_input_list = user_input.split()
    return user_input_list


def return_input_number(random_num_list, user_input_list):
    """given a random number list and a user input list that
       contains a plus-minus sign and two digits, returns a
       integer for further arithmetic operation.

    Args:
        random_num_list (list): a list that contains five random integers from a dice
        user_input_list (list): a user input list that contains a plus-minus sign,
                                  a string that indicates the postion of the tens digit,
                                  and a string indicates the postion of the units digit.
    Example: 
        if the random_num_list is [1, 3, 5, 2, 3], and the user_input_list is ["-", "2", "1"]
        then the output should be -31.

    Returns:
        integer: combined with a plus-minus sign and tens digit and units digit.
    """
    plus_minus_sign = user_input_list[0]
    tens_digit_position = int(user_input_list[1])
    units_digit_position = int(user_input_list[2])
    add_subtract_num = list_extractor(
        random_num_list, tens_digit_position, units_digit_position)
    if plus_minus_sign == "+":
        add_subtract_num *= 1
    if plus_minus_sign == "-":
        add_subtract_num *= -1
    return add_subtract_num


def dice_roller(round_number):
    """rolls the dice, asks for user input, calculates the result,
       and prints it put"

    Args:
        round_number (interger): the nth round of dicing
    """
    print("Round " + str(round_number))
    random_number_list = random_num_generator(5)
    print("The dice:" + str(random_number_list))
    user_input_list = user_input_handler()
    user_number = return_input_number(random_number_list, user_input_list)
    global ACCUMULATED_NUMBER
    ACCUMULATED_NUMBER += user_number
    print("The number: " + str(user_number))


def rounds_controller(number_of_rounds):
    """rolls the dice randomly every round, calls dice_roller(...arg) method
       to print out game information, and repeats the game for the given amount
       of rounds.

    Args:
        number_of_rounds (global variable): how many rounds of dicing in total
    """
    index = 1
    while index <= number_of_rounds:
        dice_roller(index)
        print()
        if index < number_of_rounds:
            print("Current total: " + str(ACCUMULATED_NUMBER))
            print()
            print()
        index += 1


def print_header(number_of_stars, number_of_goal):
    """prints out header of stars with format

    Args:
        number_of_stars (global variable): default to 42 for header
        number_of_goal (global variable): default to 20
    """
    print("*" * number_of_stars)
    print("REACH " + str(number_of_goal) +
          " IN THREE ROUNDS! CURRENT TOTAL: 0")
    print("*" * number_of_stars)
    print()


def print_footer(number_of_stars, current_number, number_of_goal):
    """prints out footer of stars with format

    Args:
        number_of_stars (global variable): default to 16 for footer
        current_number (global variable): accumulated total number
        number_of_goal (global variable): default to 20
    """
    print()
    print("*" * number_of_stars)
    print("Final total: " + str(current_number))
    out_number = current_number - number_of_goal
    print("Out by: " + str(out_number))
    print("*" * number_of_stars)


def main():
    """prints out header, 
       the game info, 
       and the footer
    """
    print_header(HEADER_STAR_NUMBER, GOAL_NUMBER)
    rounds_controller(ROUNDS_NUMBER)
    print_footer(FOOTER_STAR_NUMBER, ACCUMULATED_NUMBER, GOAL_NUMBER)


if __name__ == "__main__":
    main()
