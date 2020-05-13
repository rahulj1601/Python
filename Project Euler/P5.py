smallest_multiple=None
current= 2520
test= [11,12,13,14,15,16,17,18,19,20]

while smallest_multiple==None:

    current+=20

    for i in test:

        if current%i!=0:
            break

        else:

            if i==20:
                smallest_multiple=current



print(current)

            
    
    
