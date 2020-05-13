num = 600851475143
x = True
i = 2

while x == True:
    if i == num:
        print(int(num))
        x=False
    elif (num%i == 0) and (i != num):
        num = num/i
        i = 2
    else:
        i+=1
        
    

