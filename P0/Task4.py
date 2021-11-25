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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def print_arr_elements(arr, sort=True):

    if sort == True:
        arr.sort()
        for e in arr:
            print(e)
    else:
        for e in arr:
            print(e)

outgoing_calls = set()
incoming_calls = set()

outgoing_texts = set()
incoming_texts = set()

for call in calls:
    outgoing_calls.add(call[0])
    incoming_calls.add(call[1])

for text in texts:
    outgoing_texts.add(text[0])
    incoming_texts.add(text[1])

possible_telemarketers = list(outgoing_calls - (incoming_calls | outgoing_texts | incoming_texts))
print("These numbers could be telemarketers: ")
print_arr_elements(possible_telemarketers)
