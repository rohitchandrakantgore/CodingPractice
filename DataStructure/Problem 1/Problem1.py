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
    array_size = int(input("Enter the Size Of Array : "))

    array_list = list()
    for i in range(array_size) :
        array_list.append(int(input("Enter {} element : ".format(i))))
        
    # print(array_list)

    arr = array('i', array_list)
    
    result = sort012(arr,array_size)
    print(result)



############    Result  #########
# Enter the Size Of Array : 4
# Enter 0 element : 0
# Enter 1 element : 1
# Enter 2 element : 0
# Enter 3 element : 0
# array('i', [0, 0, 0, 1])