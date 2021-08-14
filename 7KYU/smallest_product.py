def smallest_product(a):
    
    smallest_product = 1000000000
    
    for array in a:
        current_product = 1
        for number in array:
            current_product *= number
        if current_product <= smallest_product:
            smallest_product = current_product
            
    return smallest_product