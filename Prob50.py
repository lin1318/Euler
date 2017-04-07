import math
def is_prime(n):
    flag=0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            flag=1
            break
    if flag==0:
        return True
    else:
        return False
l1=[2]
n=1
maxn=1000000
l3=[0 for i in range(maxn+1)]
for i in range(3,maxn+1):
    if is_prime(i):
        l1.append(i)
        l3[i]=1
lt=0
rt=1
ans=0
n=len(l1)
sum=0
while(lt<n):
    p=1
    aa=l1[lt]
    for j in range(lt+1,n):
        aa+=l1[j]
        p+=1
        if(aa>maxn):
            rt=j
            break
        if l3[aa]==1:
            if p>ans:
                ans=p
                sum=aa
    lt=lt+1
print(ans,' ',sum)




