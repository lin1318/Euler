l=[-1 for i in range(60000001)]
def dp(n):
    if(n>60000000):
        if n%2==1:
            return 1+dp(n*3+1)
        else:
            return 1+dp(n//2)
    if l[n]==-1:
        if n%2==1:
            l[n]=1+dp(n*3+1)
        else:
            l[n]=1+dp(n//2)
    return l[n]
mx=0
l[1]=1
j=0
for i in range(1,1000001):
    ans=dp(i)
    if mx<ans:
        mx=ans
        j=i
print(j)
