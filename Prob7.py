import math
def is_prime(n):
    j=int(math.sqrt(n))
    flag=0
    for i in range(2,j+1):
        if(n%i==0):
            flag=1
            break
    if(flag==0):
        return 1
    else:
        return 0
n=10001
k=0
i=2
while(k<n):
    if(is_prime(i)==1):
        k+=1
    i+=1
    if(k==n):
        break
print(i-1)