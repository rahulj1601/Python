primeSum = 0

for num in range(2,2000000):
    prime = True
    for i in range(2,num):
        if num%i == 0:
            prime=False
    if prime:
        primeSum += num

print(primeSum)
