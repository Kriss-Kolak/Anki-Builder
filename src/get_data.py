import csv
import os

def get_data_from_csv(file_name: str) -> list[tuple]:
    if not os.path.exists(file_name):
        raise Exception("Path does not exist!")
    if not os.path.isfile(file_name):
        raise Exception("Path is not a file!")
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=";", )
        result = []
        for row in reader:
            result.append(tuple(row))
        return result
    
