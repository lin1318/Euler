def doit(n,k,l):
    while n>0:
        l.append(n%k)
        n=n//k
sum=0
for i in range(1000000):
    l=[]
    l1=[]
    doit(i,2,l)
    doit(i,10,l1)
    if l==l[::-1] and l1==l1[::-1]:
        sum+=i
print(sum)

