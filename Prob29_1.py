def check(n):
    k=0
    for i in range(len(l)):
        if l[i]==n:
            k=1
            break
    if k==1:
        return False
    else:
        return True
l=[]
for a in range(2,101):
    for b in range(2,101):
        if (check(a**b)):
            l.append(a**b)
print(len(l))