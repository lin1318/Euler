f=open('D:/p042_words.txt',)
s=''
for line in f.readlines():
    s=s+line.replace('"','')
s=s.split(',')
l=[n*(n+1)//2 for n in range(100)]
sum=0
for ss in s:
    k=0
    for j in ss:
        k+=ord(j)-64
    if k in l:
        sum+=1
print(sum)
f.close()