import random

def read_random_data_from_file(file_name):
    result = []
    with open(file_name, 'r', encoding='utf8') as datafile:
        for line in datafile:
            result.append(line.strip('\n'))
        random_number = number = random.randint(0, len(result)-1)
        return result[random_number]
    
