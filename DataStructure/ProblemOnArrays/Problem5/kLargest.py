def findKthLargest(array_list,k):
    # array_list.sort()
    for i in range(len(array_list)):
        for j in range(i+1, len(array_list)):
            if(array_list[i]<array_list[j]):
                temp = array_list[i]
                array_list[i] = array_list[j] 
                array_list[j] = temp
    print(array_list)
    number = array_list[k-1]
    return number

if __name__ == "__main__":
    test_cases = int(input("Test cases : ")) 
    for i in range(1, test_cases+1):
        
        array_size = int(input("Size : "))
        array_list = list()
        for j in range(array_size):
            array_list.append(int(input("{} : ".format(j))))
    
        k = int(input('K : '))
        result = findKthLargest(array_list,k)
        print("K Number after sort: ", result)


#######    Result  ########

# Test cases : 2
# Size : 5
# 0 : 3
# 1 : 4
# 2 : 5
# 3 : 7
# 4 : 21
# K : 3
# [21, 7, 5, 4, 3]
# K Number after sort:  5
# Size : 6
# 0 : 12
# 1 : 43
# 2 : 65
# 3 : 87
# 4 : 34
# 5 : 456
# K : 2
# [456, 87, 65, 43, 34, 12]
# K Number after sort:  87