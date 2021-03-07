def nested_loop_question(number):
    value = 0
    execute =  0
    for i in range(number):
        for j in range(i, 0 , -1):
            value += j
            execute += 1
    print("execute", execute) 
    return value


if __name__ == "__main__":
    input_number_max = 100
    nested_loop_question(7)
    # for i in range(input_number_max):
    #     output = nested_loop_question(i)
    #     if output == 84:
    #         print("output = 20, i: " + str(i) )