"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""



def find_it(seq):
    
    digit_counter = {}
    
    for number in seq:
        if number in digit_counter:
            digit_counter[number] += 1
        else:
            digit_counter[number] = 1
            
    for digit, amount in digit_counter.items(): 
        if amount % 2 != 0:
            return digit
    
    return None

"""
optimal:

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
"""