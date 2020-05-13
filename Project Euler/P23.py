import time
from math import sqrt

def is_abundant(num):
    
    divSum = 1
    
    for i in range(2,int(0.5*num)+1):
        if num % i == 0:
            divSum += i
    return divSum > num


def main():

    start = time.time()
    
    upp_limit = 28123
    total = 0

    abundantNums = set(x for x in range(1,upp_limit) if is_abundant(x))
    #sets are faster to iterate through than lists
    print(time.time() - start)

    numbers = list(range(1,upp_limit))
    
    total = 0
    for i in numbers:
        sumTwoAbundants = False
        for k in abundantNums:
            if k > i/2:
                break

            if (i-k) in abundantNums:
                sumTwoAbundants = True
                break

        if not sumTwoAbundants:
            total+=i

    print(total)

    print(time.time() - start)

main()
