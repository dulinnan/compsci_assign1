def get_perepere_char(perepere_type):
    if perepere_type == 1:
        perepere_char = "0"
    elif perepere_type == 2:
        perepere_char = "X"
    else:
        perepere_char = " "
    return perepere_char

def get_perepere(position, position_list):
    output = "[ ]"
    if 1 <= position < 9:
        perepere_char = get_perepere_char(position_list[position])
        output = perepere_char
    return output

if __name__ == "__main__":
    position_list = [0, 1, 1, 1, 1, 2, 2, 2, 2]
    print(get_perepere(0, position_list))
    print(get_perepere(1, position_list))
    print(get_perepere(5, position_list))