# The Else Clause with Loops

count = 0
while count<5:
    print(count)
    count+=1
else:
    print("count value reached %d" %(count))

for i in range(1,10):
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
        
