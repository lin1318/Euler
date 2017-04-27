def cal(n):
    k=0
    while n>0:
        k+=(n%10)**5
        n//=10
    return k
sum=0
for i in range(2,1000000):
    if cal(i)==i:
        sum+=i
print(sum)