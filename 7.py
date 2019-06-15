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

def n_prime(nb):
    count,i=1,1
    while count<nb:
        i+=2
        if is_prime(i):
            count+=1
        
    return i

print(n_prime(10001))