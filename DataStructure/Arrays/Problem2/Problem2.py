
from array import array

def xorOps(arr, n):
    # print(arr)
    listArray = arr.tolist()
    # print(listArray)
    # listArray.sort()
    print(listArray)
    count = 0

    for i in range(0,len(listArray)):
        for j in range(i+1,len(listArray)):
            if (listArray[i] ^ listArray[j])==0:
                count += 1
            else:
                continue

    return count

if __name__ == "__main__":

    test_cases = int(input("Enter Number of Test cases : ")) 
    for i in range(1, test_cases+1):
        
        array_size = int(input("Enter the Size Of {} Array : ".format(i)))

        array_list = list()
        array_list.append(int(input("Enter Array elements")))
        # for j in range(array_size):
        #     array_list.append(int(input("Enter Array : "))
        
        arr = array('i', array_list)
    
        result = xorOps(arr,array_size)
        print("Count : ",result)



##########  Result  #########
# Enter Number of Test cases : 2
# Enter the Size Of 1 Array : 5
# Enter 0 element of 1 Array : 1
# Enter 1 element of 1 Array : 3
# Enter 2 element of 1 Array : 4
# Enter 3 element of 1 Array : 1
# Enter 4 element of 1 Array : 4
# [1, 1, 3, 4, 4]
# Count :  2

# Enter the Size Of 2 Array : 3
# Enter 0 element of 2 Array : 2
# Enter 1 element of 2 Array : 2
# Enter 2 element of 2 Array : 2
# [2, 2, 2]
# Count :  3