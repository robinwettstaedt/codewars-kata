def sum_of_digits(digits): 
    
    if not digits and digits != 0: 
        return ""
    
    if type(digits) is int:
        digits = str(digits)
    
    list = [digit for digit in digits]
    list_of_digits = enumerate(list)
    output = ""
    result = 0
    
    for index, number in list_of_digits:
        result += int(number)
        if index == len(list)-1:
            output += f"{number} "
        else:
            output += f"{number} + "
        
    output += f"= {result}"
    
    return output