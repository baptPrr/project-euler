def find_abc(nb):
    for c in range(1,999):
        for b in range(1,c):
            for a in range(1,b):
                if a + b + c == 1000:
                    if a**2 + b**2 == c**2:
                        return a,b,c
                else:
                    continue

re = find_abc(1000)
print(re[0]*re[1]*re[2])
