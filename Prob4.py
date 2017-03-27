def check(n):
    s=str(n)
    if(s==s[::-1]):
        return 1
    else:
        return 0
max=0
for x in range(100,1000):
    for y in range(100,1000):
        ans=x*y
        if(check(ans)==1):
            if(max<ans):
                max=ans
print(max)