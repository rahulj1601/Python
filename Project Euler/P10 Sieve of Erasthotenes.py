import math

n = 2000000
nums=[]
for each in range(2,n+1):
    nums.append(each)

index=-1
p=2
while p <= math.sqrt(n):
    index+=1
    p=nums[index]
    
    for i in range(p*2,n+1,p):
        if i in nums:
            nums.remove(i)

total=0
for j in nums:
    total+=j
print(total)
    
