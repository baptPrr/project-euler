def reverse(x):
    x_rev=''
    for i in range(1,len(x)+1):
        x_rev+=x[-i]
    return x_rev


def palindrom_number(x):
    palindrom=False
    lon = len(x)
    if lon%2==0:
        if x[:int(lon/2)] == reverse(x[int(lon/2):]): 
            palindrom = True
    else:
        if x[:lon//2] == reverse(x[lon//2+1:]):
            palindrom = True
    return palindrom

def two_digit_product_palindrom():
    m,n = 999,999
    palindrom=[]
    while m>500:
        test = m*n
        if palindrom_number(str(test)):
            palindrom.append((m,n,test))
        if n==100:
            m-=1
            n=m
        else:
            n-=1
    return palindrom

print(sorted(two_digit_product_palindrom(),key= lambda x:x[2],reverse=True)[0])