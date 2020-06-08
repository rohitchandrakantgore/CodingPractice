
def findLargest(numList):
    for i in range (len(numList)):
        for j in range (i+1, len(numList)):
            if (numList[i]+numList[j]<numList[j]+numList[i]):
                temp = numList[i]    
                numList[i] = numList[j]  
                numList[j] = temp
    # print(numList)
    str = ''
    largestNumber = str.join(numList)
    
    return largestNumber

if __name__ == "__main__":
    test_cases = int(input("Test cases : ")) 
    for i in range(1, test_cases+1):
        
        array_size = int(input("Size : "))
        array_list = list()
        for j in range(array_size):
            array_list.append(input("{} : ".format(j)))
    
        result = findLargest(array_list)
        print("Largest Possible Number is : ", result)


########  Result  ########

# Test cases : 2
# Size : 5
# 0 : 3
# 1 : 30
# 2 : 34
# 3 : 5
# 4 : 9
# Largest Possible Number is :  9534330
# Size : 4
# 0 : 54
# 1 : 546
# 2 : 548
# 3 : 60
# Largest Possible Number is :  6054854654