import math
i=1
while 1:
    n=i*(i+1)//2
    k=2
    for j in range(2,int(math.sqrt(n))):
       if n%j==0:
           k+=2
    if k>500:
        print(n)
        break
    i+=1