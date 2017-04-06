l=[[] for i in range(100)]
dp=[[0 for i in range(100)] for i in range(100)]
i=0
f=open('D:/p067_triangle.txt','r')
for a in f.readlines():
    a=a.strip()
    l[i]=a.split()
    i+=1
dp[0][0]=int(l[0][0])
ans=dp[0][0]
for i in range(1,100):
    dp[i][0]=dp[i-1][0]+int(l[i][0])
    ans=max(dp[i][0],ans)
    dp[i][i]=dp[i-1][i-1]+int(l[i][i])
    ans=max(dp[i][i],ans)
for i in range(1,100):
    for j in range(1,i):
        dp[i][j]=int(l[i][j])+max(dp[i-1][j],dp[i-1][j-1])
        ans=max(dp[i][j],ans)
print(ans)
