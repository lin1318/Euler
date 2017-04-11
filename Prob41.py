import math
global ans
def cal(s):
    sum=0;
    for i in range(len(s)):
        sum=sum*10+s[i]
    return sum
def is_prime(n):
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            return False
    return True
def dfs(k):
    global ans
    if k==7:
        #print(a)
        if is_prime(cal(a)) and cal(a)>ans:
            ans=cal(a)
    else:
        for i in range(1,8):
            if tag[i]==0:
                tag[i]=1
                a.append(i)
                dfs(k+1)
                tag[i]=0
                a.pop()

tag=[0 for i in range(10)]
ans=0
a=[]
dfs(0)
print(ans)