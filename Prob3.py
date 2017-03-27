n=600851475143
i=2
ans=0
while n>1:
    while n%i==0:
        n=n/i
        ans=i
    i=i+1
print(ans)