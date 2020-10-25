def insecure_hash(password):
    ascii_code_list = []
    mod_11_code_list = 0
    for char in password:
        ascii_code_list.append(ord(char))
    for code in ascii_code_list:
        mod_11_code_list += (code % 11)
    print(mod_11_code_list)
    print(chr(mod_11_code_list))


if __name__ == "__main__":
    password = "aedg2565560984"
    insecure_hash(password)
