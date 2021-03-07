def is_between_or_even(test_value, low_value, high_value):
    if low_value <= test_value <= high_value and round(test_value,2)==test_value:
        return True
    return False

def main():
    print(is_between_or_even(23.99, 22.0, 24))
    # print(23.99>=22.0)
    # print((23.99-24)<0)

if __name__ == "__main__":
    main()