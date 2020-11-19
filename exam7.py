def function1(number):
    boolean = -5 <= number <= 15
    return boolean


def function2(number):
    boolean = ((number % 2 != 0) and (number % 7 != 0))
    return boolean


def function3(name):
    boolean = (len(name) >= 7) and ((name[0] == "S") or (name[0] == "F"))
    return boolean


def function4(word):
    boolean = (word[-3:] == "ing") and ("r" not in word)
    return boolean


if __name__ == "__main__":
    output1 = function1(1)
    output2 = function2(21)
    print("output2: ",output2)
    print(type(output2))
    output3 = function3("Players")
    print("output3: ", output3)
    print(type(output3))
    output4 = function4("Rowing")
    print("output4: ", output4)
    print(type(output4))
