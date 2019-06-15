import numpy as np
from collections import Counter

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

def get_primes(nb):
    x=1
    primes=[]
    while x<nb:
        if is_prime(x):
            primes.append(x)
        x+=1
    return primes


def decompo_primes(nb,primes,factors):
    nbt=nb
    decomp_primes = []
    while is_prime(nbt)==False:
        for i in primes:
            if nbt%i==0:
                decomp_primes.append(i)
                nbt /= i
                break
    decomp_primes.append(int(nbt))
    factor = Counter(decomp_primes)
    for prime in factors:
        if factor[prime] and factor[prime] > factors[prime]:
            factors[prime]=factor[prime]
    return factors


def PPCM(nb):
    primes = get_primes(nb)
    factors={k:0 for k in primes}
    ppcm=1
    for i in range(2,nb+1):
        factors = decompo_primes(i,primes,factors)
        # print('decompo ',i,' done')
        print('étape ',i,': ',factors)
    for i in factors:
        ppcm *= i**factors[i]
    return ppcm

print(PPCM(20))
# 232792560



