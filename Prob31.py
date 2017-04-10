l=[1 for i in range(1,202)]
for i in range(199):
    l[i+2]+=l[i]
for i in range(196):
    l[i+5]+=l[i]
for i in range(191):
    l[i+10]+=l[i]
for i in range(181):
    l[i+20]+=l[i]
for i in range(151):
    l[i+50]+=l[i]
for i in range(101):
    l[i+100]+=l[i]
l[200]+=1
print(l[200])