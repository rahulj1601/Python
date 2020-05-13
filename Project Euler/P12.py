from functools import reduce
n = 5

while True:

    triNum = (n/2) * (n+1)
    n += 1

    i = 2
    dic = {}
    
    while i <= triNum:
        
        if triNum % i == 0:
            triNum = triNum/i
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1   
            i = i-1
        i += 1

    powers = map(lambda x:(x+1), dic.values())
    divisors = reduce(lambda x,y:x*y, powers)

    if divisors > 500:
        n-=1
        print((n/2)*(n+1))
        break
