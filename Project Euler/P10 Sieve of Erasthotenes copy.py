n = 2000000

nums=[]
for each in range(2,n):
    nums.append(each)
    
x=True
index=-1

while x==True:
    index+=1
    p=nums[index]
    
    for i in nums:
        if i==p:
            continue
        elif i%p==0:
            nums.remove(i)
            
    if p**2 > n:
        x=False

total=0
for j in nums:
    total+=j
    
print(total)
    
