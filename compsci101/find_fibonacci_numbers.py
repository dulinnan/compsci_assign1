def find_fibonacci_numbers(start_position, end_position):
    fibonacci_sequence = [0, 1]
    for index in list(range(2, 200)):
        fibonacci_sequence.append(
            fibonacci_sequence[index-1] + fibonacci_sequence[index-2])
    return fibonacci_sequence[start_position-1:end_position]


if __name__ == "__main__":
    print(find_fibonacci_numbers(3, 10))
    print(find_fibonacci_numbers(11, 20))
