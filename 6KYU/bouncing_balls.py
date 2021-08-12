def bouncing_ball(h, bounce, window):
    
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        
        total_bounce = h * bounce
        number_of_sights = 1
        
        if window > total_bounce:
            return number_of_sights
        
        while window < total_bounce:
            number_of_sights += 2
            total_bounce *= bounce
        
        return number_of_sights
    
    return -1

