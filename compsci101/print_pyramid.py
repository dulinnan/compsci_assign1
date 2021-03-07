def print_pyramid(number_of_rows):
    for i in range(number_of_rows):
        for j in range(number_of_rows):
            if (i == j):
                print(' '*(number_of_rows-i-1) + '*'*(2*j+1))


if __name__ == "__main__":
    print_pyramid(8)
