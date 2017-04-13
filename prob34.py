def fact(n):
    ans=1
    for i in range(1,n+1):
        ans*=i
    return ans
def dight(n):
    ans=0
    while(n>0):
        ans=ans+fact(n%10)
        n=n//10
    return ans
sum=0
for i in range(1,100000):
    if(dight(i)==i):
        sum+=i
print(sum-3)