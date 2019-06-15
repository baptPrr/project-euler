import time

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


def sum_primes(nb):
    somme=2
    for i in range(3, nb,2):
        if is_prime(i):
            somme+=i
    return somme
deb=time.time()
print(sum_primes(2000000),'\n',time.time()-deb)