def check(a,b,c):
    l=[0 for i in range(0,10)]
    nc=0
    c1=c
    while c>0:
      l[c%10]+=1
      c=c//10
    while a > 0:
        l[a % 10] += 1
        a = a // 10
    while b > 0:
        l[b % 10] += 1
        b = b // 10
    flag=0
    for i in range(1,10):
        if l[i]!=1:
            flag=1
            break
    if l[0]!=0:
        flag=1
    if flag==0:
        return True
    else:
        return False

a=[]
for i in range(1,2000):
    for j in range(1,1000):
        if(check(i,j,i*j)):
            n=len(a)
            flag=0
            for k in range(0,n):
                if a[k]==i*j:
                    flag=1
                    break
            if flag==0:
                a.append(i*j)
sum=0
for i in range(0,len(a)):
    sum+=a[i]
print(sum)

