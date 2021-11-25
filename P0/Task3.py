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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


import re

def is_Bangalore(number):

    if number[:5] == '(080)':
        return True
    return False

def get_area_code(number):
    
    # credit to the answer from https://stackoverflow.com/questions/4894069/regular-expression-to-return-text-between-parenthesis
    # for extracting the number between parenthesis
    if number[0] == '(':
        return number[number.find('('):number.find(')') + 1]
    elif number[:3] == '140':
        return '140'
    else:
        return number[:4]

def print_arr_elements(arr, sort=True):

    if sort == True:
        arr.sort()
        for e in arr:
            print(e)
    else:
        for e in arr:
            print(e)
    

def percentage(numerator, denominator, decimals = 2):

    return round(100 * float(numerator) / denominator, decimals)
    

# part A
called_from_Bangalore_codes = set()
called_from_Bangalore_codes_list = []

for call in calls:

    calling_number = call[0]
    receiving_number = call[1]
    receiving_number_area_code = get_area_code(receiving_number)
    receiving_number_area_code_duplicate = receiving_number_area_code in called_from_Bangalore_codes

    if is_Bangalore(calling_number) and not receiving_number_area_code_duplicate:
        called_from_Bangalore_codes.add(receiving_number_area_code)
        called_from_Bangalore_codes_list.append(receiving_number_area_code)

print_arr_elements(called_from_Bangalore_codes_list)

      
# part B

bangalore_to_bangalore = 0
bangalore_to_any = 0
for call in calls:

    calling_number = call[0]
    receiving_number = call[1]
    
    if is_Bangalore(calling_number):
        bangalore_to_any += 1
        if is_Bangalore(receiving_number):
            bangalore_to_bangalore += 1

percent_bangalore_to_bangalore = percentage(bangalore_to_bangalore, bangalore_to_any)

print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(percent_bangalore_to_bangalore))
        