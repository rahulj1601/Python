def even(n):
    return n/2

def odd(n):
    return (3*n)+1

def collatz(num):
    seqLen = 1
    while num != 1:
        if num % 2 == 0:
            num = even(num)
        else:
            num = odd(num)
        seqLen += 1
    return seqLen
    
def main():
    chainLen = 10
    num = 13
    for i in range(13,1000000):
        funcRun = collatz(i)
        if funcRun > chainLen:
            chainLen = funcRun
            num = i
    print(num)

main()
            
