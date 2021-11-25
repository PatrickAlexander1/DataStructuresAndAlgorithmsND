"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def get_number_count(*args):

    unique_numbers = set()
    total_unique_numbers = 0
    for data in args:
        for element in data:
            sending_number, receiving_number = element[0], element[1]
            if sending_number not in unique_numbers:
                total_unique_numbers += 1
                unique_numbers.add(sending_number)
            if receiving_number not in unique_numbers:
                total_unique_numbers += 1
                unique_numbers.add(receiving_number)

    return total_unique_numbers

total_unique_numbers = get_number_count(calls,texts)
    
print("There are {} different telephone numbers in the records.".format(total_unique_numbers))