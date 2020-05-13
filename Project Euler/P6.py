squareSum = 0
total = 0

for i in range(1,101):
    squareSum += i**2
    total += i

totalSquared = total**2

print(totalSquared - squareSum)
