multiply = 1
total = 0

for i in range(1,101):
    multiply *= i

for num in list(str(multiply)):
    total += int(num)

print(total)
