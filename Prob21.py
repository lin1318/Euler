def dd(n):
    p=0
    for i in range(1,n):
        if n%i==0:
            p+=i
    return p

sum=0
for i in range(1,10001):
    a=dd(i)
    if dd(a)==i and a!=i:
        sum+=i
print(sum)