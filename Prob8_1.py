f=open("D:\data.txt",'r')
s=f.read()
max=1
for i in range(0,len(s)-12):
    ans=1
    for j in range(0,13):
        ans=ans*int(s[i+j])
    if(ans>max):
        max=ans
print(max)
f.close()
