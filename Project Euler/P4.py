maxPalindrome = 0

for i in range(100,1000):
    for j in range(100,1000):
        product = i * j
        productStr = str(product)
        if (productStr[0] == productStr[-1]) and (productStr[1] == productStr[-2]) and (productStr[2] == productStr[-3]):
            if maxPalindrome < product:
                maxPalindrome = product

print(maxPalindrome)
