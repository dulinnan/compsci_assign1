def function1(number_string, base):
    """
    Iterate thru the list, which has length greater than 0,
    calculate the result, and return it.

    >>> function1([], 0)
    0
    >>> function1(None, 0)
    Traceback (most recent call last):
        ...
    TypeError: object of type 'NoneType' has no len()
    >>> function1([], None)
    None
    """
    value = 0
    power = 0
    for i in range(len(number_string)-1, -1, -1):
        value += int(number_string[i])*base**power
        power += 1
    return value


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # input_list = None
    # input_base = 0
    # output = function1(input_list, input_base)
    # print(output)

