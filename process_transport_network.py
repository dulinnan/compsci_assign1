def print_dictionary(data_dict):
    key_list = list(data_dict.keys())
    key_list.sort()
    for key in key_list:
        print(key, ": ", data_dict[key], sep="")


def process_transport_network(file_name):
    with open(file_name) as f:
        read_name_list = f.readlines()
    f.close()
    sanitised_list = []
    departure_names_list = []
    destination_names_list = []
    for every_record in read_name_list:
        sanitised_record = every_record.replace("\n", "").strip()
        sanitised_record = sanitised_record.replace("(", "")
        sanitised_record = sanitised_record.replace(")", "")
        split_sanitised_record = sanitised_record.split(",")
        sanitised_list.append(split_sanitised_record)
    for each_route in sanitised_list:
        departure_name = each_route[0]
        if (departure_name not in departure_names_list):
            departure_names_list.append(departure_name)
    sorted_departure_names_list = sorted(departure_names_list)
    for each_name in list(range(len(sorted_departure_names_list))):
        destination_names_list.append([])
    index = 0
    while index < len(sorted_departure_names_list):
        sorted_departure_name = sorted_departure_names_list[index]
        for each_route in sanitised_list:
            departure_name = each_route[0]
            if(departure_name == sorted_departure_name):
                destination_names_list[index].append(each_route[1])
                destination_names_list[index].sort()
        index += 1
    index_of_destination_name = 0
    output = {}
    while index_of_destination_name < len(destination_names_list):
        output[sorted_departure_names_list[index_of_destination_name]
               ] = destination_names_list[index_of_destination_name]
        index_of_destination_name += 1
    return output


if __name__ == "__main__":
    file_name = "./AucklandTrainNetwork.txt"
    network_dict = process_transport_network(file_name)
    print_dictionary(network_dict)
