def even_and_odd(n): 
    
    list = [int(j) for j in str(n)]
    ne = 0
    no = 0
         
    for x in list:
        ne = ne*10+x if x % 2 == 0 else ne
        no = no*10+x if x % 2 != 0 else no
        
    return (ne, no)