import time
even,u_n,u_n1 =0,1,2
while u_n1 < 4000000:
	if u_n1% 2 ==0:
		even+=u_n1
	u_n,u_n1=u_n1,u_n+u_n1
print(even)
