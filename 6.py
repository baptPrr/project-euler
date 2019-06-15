def diff(nb):
    sum_square = sum([i**2 for i in range(1,nb+1)])
    square_sum = sum([i for i in range(1,nb+1)])**2
    return abs(sum_square-square_sum)

print(diff(100))