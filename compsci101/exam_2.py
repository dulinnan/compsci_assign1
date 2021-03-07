def main():
    print("main", end = " ")
    a_list = [1,2,3]
    step1(a_list)
    print(a_list)

def step1(my_list):
    print("step1", end = " ")
    my_list.append(100)
    step2(my_list)
    step3(my_list)

def step2(your_list):
    print("step2", end = " ")
    your_list[0] = 0
    step3(your_list)

def step3(my_list):
    print("step3", end = " ")
    my_list[1] += 1


if __name__ == "__main__":
    main()