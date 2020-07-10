import csv


def load_state_data(file_to_read):
    reader = csv.DictReader(file_to_read)

    for row in reader:
        pass
