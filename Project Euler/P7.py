x=0
for num in range(2,1000000000):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       x+=1
       if x==10001:
           break

print(num)


