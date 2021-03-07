def main():
    data_dict = {("Peter","Wang"): 
        (13, 13, 13, 13),
        ("Michael","Smith"): [0],
        ("Jane","Hill"): [15, 15, 15, 15],
        ("May","Jones"): [12, 12]}
    filename = "./output.txt"
    write_data(filename, data_dict)


def write_data(filename, data_dict):
    output_stream = open(filename, 'w')
    for key in data_dict:
        print("key",key)
        name = key[0] + " " + key[1]
        if (len(data_dict[key]) <= 2):
            output_stream.write(name + ": not enough data \n")

        else:
            average_mark = (sum(data_dict[key]) // len(data_dict[key]))
            output_stream.write(name + ": " + str(average_mark) + "\n")
    output_stream.close()


main()
