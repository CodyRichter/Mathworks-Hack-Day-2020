import csv


def load_state_data(file_to_read):
    data = []
    with open(file_to_read, 'r') as read_obj:
        # pass the file object to DictReader() to get the DictReader object
        csv_dict_reader = csv.DictReader(read_obj)
        # iterate over each line as a ordered dictionary
        first = True
        for row in csv_dict_reader:
            if first:
                date = row['Date'][0:row['Date'].index(' ')]
                date = int(date[0:2])
                first = False
                for index in range(date - 8):
                    data.append(None)

            data.append(row['Cases'])

    return data


# import csv
# import glob
# import json
#
#
# def load_state_data(file_to_read):
#     data = []
#     with open(file_to_read, 'r') as read_obj:
#         # pass the file object to DictReader() to get the DictReader object
#         csv_dict_reader = csv.DictReader(read_obj)
#         # iterate over each line as a ordered dictionary
#         first = True
#         for row in csv_dict_reader:
#             if first:
#                 date = row['Date'][0:row['Date'].index(' ')]
#                 date = int(date[0:2])
#                 first = False
#                 for index in range(date - 8):
#                     data.append(None)
#
#             data.append(int(row['Cases']))
#
#     return data
#
#
# state_data = {}
#
# path = "/Users/vortek/PycharmProjects/MathworksHackDay/static/datasets/*.csv"
#
# for file_name in glob.glob(path):
#     state_name = str(file_name[63:-4])
#     state_data[state_name] = json.dumps(load_state_data(file_name))
#
# for key in state_data.keys():
#     # print(key)
#     print('state_data["'+key+'"]='+"'"+state_data[key]+"'")
# pass


