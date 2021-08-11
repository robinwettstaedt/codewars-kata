def halving_sum(n): 
    
    break_check = 2
    divisor = 2
    result = n
    
    while break_check > 1:
        break_check = int(n / divisor)
        divisor *= 2
        result += break_check
        
    return result