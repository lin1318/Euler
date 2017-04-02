def dight(n):
    sum=0
    while n>0:
        sum=sum+n%10
        n=n//10
    return sum
    
k=0
l=[]
for i in range(2,100):
    for j in range(2,100):
        t=i**j
        d=dight(t)
        if d==i:
            k+=1
            l.append(t)
l=sorted(l)
print(l[29])