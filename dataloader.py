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




