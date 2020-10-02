def calculate_discount_percentage(number_of_plant, is_vip):
    discount_percent = 0
    if (is_vip):
        if 0 < number_of_plant < 10:
            discount_percent = 10
        elif 10 <= number_of_plant < 50:
            discount_percent = 20
        elif number_of_plant >= 50:
            discount_percent = 30
    else:
        if 10 <= number_of_plant < 50:
            discount_percent = 10
        if number_of_plant >= 50:
            discount_percent = 20
    return discount_percent


if __name__ == "__main__":
    print(calculate_discount_percentage(5,True))
    print(calculate_discount_percentage(10,True))
    print(calculate_discount_percentage(55,True))
    print(calculate_discount_percentage(5,False))
    print(calculate_discount_percentage(11, False))
    print(calculate_discount_percentage(49,False))
    print(calculate_discount_percentage(55,False))