"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

max_time = 0
phone_number = None
phone_numbers_with_times = {}

for call in calls:

    time, sending_number, receiving_number = int(call[-1]), call[0], call[1]

    # add the time to sending_number and receiving_number in the dictionary
    if sending_number not in phone_numbers_with_times:
        phone_numbers_with_times[sending_number] = time
    else:
        phone_numbers_with_times[sending_number] += time
    if receiving_number not in phone_numbers_with_times:
        phone_numbers_with_times[receiving_number] = time
    else:
        phone_numbers_with_times[receiving_number] += time
    
    # update the maximum time and the phone number corresponding to the maximum time
    if phone_numbers_with_times[sending_number] > max_time:
        max_time = phone_numbers_with_times[sending_number]
        phone_number = sending_number

    if phone_numbers_with_times[receiving_number] > max_time:
        max_time = phone_numbers_with_times[receiving_number]
        phone_number = receiving_number


print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone_number, max_time))