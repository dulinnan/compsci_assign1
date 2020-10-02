def matching_position(horizontal_str, vertical_str):
    pos = []
    for ia, ca in enumerate(horizontal_str):
        for ib, cb in enumerate(vertical_str):
            if ca == cb:
                pos.append((ia, ib, ca))
    return pos;

def string_builder(horizontal_str, vertical_str, hori_pos, verti_pos):
    if hori_pos == len(vertical_str):
        print(horizontal_str)
        i = 1
        while i < len(vertical_str):
            print(" " * (len(horizontal_str)-1) + vertical_str[i])
            i += 1
    
    if verti_pos == len(horizontal_str):
        while i < len(vertical_str):
            print(" " * (len(horizontal_str)-1) + vertical_str[i])
            i += 1



def word_puzzle(horizontal_str, vertical_str):
    output = ""
    matched_positions = matching_position(horizontal_str, vertical_str)
    # output = str(matched_positions)
    if matched_positions == []:
        output = "The two strings do not intersect"
        return output
    first_match = list(matched_positions)
    matched_pos_of_hori = first_match[0][0]
    matched_pos_of_verti = first_match[0][1]
    # print(str(matched_pos_of_hori))
    # print(str(matched_pos_of_verti))
    string_builder(horizontal_str, vertical_str, matched_pos_of_hori, matched_pos_of_verti)



def main():
    word_puzzle("colony", "yummy")

if __name__ == "__main__":
    main()