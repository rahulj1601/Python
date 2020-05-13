sequence = [1, 2]
num = 0

while sequence[-1] < 4000000:
    x = sequence[-1] + sequence[-2]
    sequence.append(x)

for each in sequence:
    if each % 2 == 0:
        num += each

print(num)

