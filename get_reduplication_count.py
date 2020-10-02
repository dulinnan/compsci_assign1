def get_reduplication_count(word_list):
    count = 0
    for word in word_list:
        if(len(word) % 2) == 0:
            first_half, second_half = word[:int(len(word)/2)], word[int(len(word)/2):]
            if (first_half == second_half):
                count += 1
    return count


if __name__ == "__main__":
    print(get_reduplication_count(
        ["booboo", "byebye", "cancan", "chopchop", "chilly"]))
