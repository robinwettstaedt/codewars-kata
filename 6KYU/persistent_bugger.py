"""
Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit
                  
 persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 persistence(4) # returns 0, because 4 is already a one-digit number
"""

import math

def persistence(n):
    
    if n < 10:
        return 0
    
    arr = [ int(digit) for digit in str(n)]
    counter = 0
    
    while n > 10:
        counter += 1
        n = math.prod(arr)   
        if n == 10:
            counter += 1
        arr = [int(new_digit) for new_digit in str(n)]
        
    return counter 