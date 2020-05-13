# Break and Continue Statements

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

print()

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)
