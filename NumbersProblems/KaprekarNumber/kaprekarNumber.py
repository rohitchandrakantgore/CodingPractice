



def isKaprekarNumber(num):
    numSqr = str(num**2)
    
    right = numSqr[len(numSqr)//2:]
    if (numSqr[:len(numSqr)//2]== ''):
        left = 0
    else:
        left = numSqr[:len(numSqr)//2]

    return True if int(left)+int(right) == num else False

if __name__ == "__main__":

    karpekarNumberList = list()
    for num in range(1,1000):
        if isKaprekarNumber(num):
            karpekarNumberList.append(num)
    
    print(karpekarNumberList)