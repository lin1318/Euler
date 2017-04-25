n,i,sum=2,1,1
while n<=2001:
    i += ((n - 2) // 4+1)*2
    sum+=i
    n+=1
print(sum)