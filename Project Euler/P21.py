def d(n):
    total = 0
    for i in range(1,n):
        if n % i == 0:
            total += i
    return total

def main():
    amiNums = []
    nums = [i for i in range(1,10000)]
    summation = 0
    
    for num in nums:
        if (d(d(num)) == num) and (d(num) != num):
            amiNums.append(num)
            summation += num

    print(summation)
    print(amiNums)

main()


