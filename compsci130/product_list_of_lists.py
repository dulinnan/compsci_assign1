from functools import reduce

def calculate_product_of_a_list(list_of_numbers):
    # Python3 program to multiply all values in the
    # list using lambda function and reduce()
    result = reduce((lambda x, y: x * y), list_of_numbers)
    return result


def product_list_of_lists(numbers):
    # List comprehension
    # output = [calculate_product_of_a_list(each_list) for each_list in numbers]
    # Map function
    output = list(map(lambda each_list: calculate_product_of_a_list(each_list), numbers))
    return output


if __name__ == "__main__":
    data = [[1], [3, 4, 5], [3, 2], [1, 4, 4, 1]]
    product_list_of_lists(data)
