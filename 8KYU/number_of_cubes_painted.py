def count_squares(cuts):
    amount_of_cubes = (cuts+1)**3
    amount_of_inner_cubes = (cuts-1)**3

    return amount_of_cubes - amount_of_inner_cubes  