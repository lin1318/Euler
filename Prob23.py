import math
def is_abundant(n):
    sum=1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            sum+=i
            if i*i!=n:
                sum+=(n//i)
    return sum>n
l=[i for i in range(1,28124) if is_abundant(i)]
tag=[1 for i in range(28124)]
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]+l[j]<=28123:
            tag[l[i]+l[j]]=0
sum=0
for i in range(1,28124):
    sum+=(tag[i]*i)
print(sum)