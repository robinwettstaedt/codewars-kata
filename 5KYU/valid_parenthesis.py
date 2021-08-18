"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""

def valid_parentheses(string):
    
    if len(string) == 0:
        return True
        
    if len(string) == 1:
        return False
    
    left_parenthesis_amount = 0
    right_parenthesis_amount = 0
    
    for c in string:
        if c == "(":
            left_parenthesis_amount += 1
        
        if c == ")":
            right_parenthesis_amount += 1
            
        if right_parenthesis_amount > left_parenthesis_amount:
            return False
        
    if left_parenthesis_amount == right_parenthesis_amount:
        return True
    
    return False