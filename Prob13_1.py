f=open("D:\data.txt",'r')
s=""
sum=0
for x in f.readlines():
    s=x.strip()
    sum+=int(s)
print(sum)
f.close()