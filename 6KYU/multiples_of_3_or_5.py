def solution(number):
    
    result = 0
    
    for i in range(number):
        if i % 5 == 0 or i % 3 == 0:
            result += i
    
    return result