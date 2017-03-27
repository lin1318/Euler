ans1=0
ans2=0
for i in range(101):
    ans1=ans1+i*i
for i in range(101):
    ans2=ans2+i
ans2=ans2*ans2
print(ans2-ans1)