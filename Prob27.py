import math
def is_prime(n1):
    if(not isinstance(n1, (int))):
        return False
    if n1<0:
        return False
    for i in range(2, int(math.sqrt(n1))):
        if n1%i == 0:
            return False
    return True
ans=0
j=0
for a in range(-1000,1001):
    for b in range(-1000,1001):
        n=0
        while(is_prime(n*n+a*n+b)):
            n+=1
        if n>j:
            ans=a*b
            j=n
print(ans)