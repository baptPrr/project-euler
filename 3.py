def is_prime(x):
    prime = True
    if x==1:
        prime=False
    if x==2:
        prime=True
    elif x%2==0:
        prime=False
    else:
        for i in range(3,int(x**0.5)+1,2):
            if x%i==0:
                prime=False
                break
    return prime

def biggest_prime_dividor(x):
    i=int(x**0.5)+1
    while i > 0:
        if x%i==0:
            if is_prime(i):
                break
        i-=1
    return i


print(biggest_prime_dividor(600851475143))