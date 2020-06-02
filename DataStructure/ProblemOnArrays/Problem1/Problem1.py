# Given an array of size N containing 0s, 1s, and 2s; sort the array in ascending order.

# Input:
# First line of input contains number of testcases T. For each testcase, there will be two lines, first of which will contain N. The second lines contains the elements of the array.
# Output: 
# Print sorted array.
# Example:
# Input :
# 2
# 5 0 0
# 0 2 0 2 0

# Output:
# 0 0  
# 0 0 0 2 2

from array import array

def sort012(arr, n):
    # print(arr)
    listArray = arr.tolist()
    # print(listArray)

    for i in range(0,n):
        for j in range(i+1, n):
            if(listArray[i]>listArray[j]):
                temp = listArray[i];    
                listArray[i] = listArray[j];    
                listArray[j] = temp;     

    new_list = []
    for i in range(0,len(listArray)):
        if listArray[i]<3:
            new_list.append(listArray[i])

    resultArray = array('i',new_list)
    return resultArray

if __name__ == "__main__":
    test_cases = int(input("Enter Number of Test cases : ")) 
    for i in range(1, test_cases+1):
        
        array_size = int(input("Enter the Size Of {} Array : ".format(i)))

        array_list = list()
        
        for j in range(array_size):
            array_list.append(int(input("Enter {} element of {} Array : ".format(j,i))))
        
        arr = array('i', array_list)

        result = sort012(arr,array_size)
        print("Result Array", result)



############    Result  #########
# Enter Number of Test cases : 2
# Enter the Size Of 1 Array : 3
# Enter 0 element of 1 Array : 1
# Enter 1 element of 1 Array : 0
# Enter 2 element of 1 Array : 0
# Result Array array('i', [0, 0, 1])
# Enter the Size Of 2 Array : 5
# Enter 0 element of 2 Array : 1
# Enter 1 element of 2 Array : 0
# Enter 2 element of 2 Array : 2
# Enter 3 element of 2 Array : 0
# Enter 4 element of 2 Array : 1
# Result Array array('i', [0, 0, 1, 1, 2])
