def convertToWords(num):
    numWords = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'onehundred',200:'twohundred',300:'threehundred',400:'fourhundred',500:'fivehundred',600:'sixhundred',700:'sevenhundred',800:'eighthundred',900:'ninehundred'}

    if len(str(num)) == 1:
        return numWords.get(num)

    elif len(str(num)) == 2:
        if num in numWords.keys():
            return numWords.get(num)
        else:
            return numWords.get(int(str(num)[0] + "0")) + numWords.get(int(str(num)[1]))

    elif len(str(num)) == 3:
        if num in numWords.keys():
            return numWords.get(num)
        elif str(num)[1] == "0":
            return numWords.get(int(str(num)[0])) + "hundredand" + numWords.get(int(str(num)[2]))
        elif int(str(num)[1:]) in numWords.keys():
            return numWords.get(int(str(num)[0])) + "hundredand" + numWords.get(int(str(num)[1:]))
        else:
            return numWords.get(int(str(num)[0])) + "hundredand" + numWords.get(int(str(num)[1] + "0")) + numWords.get(int(str(num)[2]))

    else:
        return "onethousand"

def main():
    
    totalLetters = 0
    for num in range(1,1001):
        totalLetters += len(convertToWords(num))
    print(totalLetters)

main()
