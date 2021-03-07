def print_numbers_triangle(number_of_rows):
    for i in range(number_of_rows+1, 1, -1):
        for j in range(1, i):
            print(j, end="")
        print()


if __name__ == "__main__":
    print_numbers_triangle(8)
