def check_palindrome(text):
    i = 0
    pure_string = ""
    if len(text) == 0:
        return True
    while i < len(text):
        if str(text[i]).isalpha():
            pure_string += text[i].upper()
        i += 1

    rev = ''.join(reversed(pure_string))
    if (pure_string == rev):
        return True
    return False


if __name__ == "__main__":
    print(check_palindrome("Hello World!"))
