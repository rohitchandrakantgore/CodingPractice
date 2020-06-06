def findKthSmaller(array_list,k):
    # array_list.sort()
    for i in range(len(array_list)):
        for j in range(i+1, len(array_list)):
            if(array_list[i]>array_list[j]):
                temp = array_list[i]
                array_list[i] = array_list[j] 
                array_list[j] = temp
    print(array_list)
    smallestNumber = array_list[k-1]
    return smallestNumber

if __name__ == "__main__":
    test_cases = int(input("Test cases : ")) 
    for i in range(1, test_cases+1):
        
        array_size = int(input("Size : "))
        array_list = list()
        for j in range(array_size):
            array_list.append(int(input("{} : ".format(j))))
    
        k = int(input('K : '))
        result = findKthSmaller(array_list,k)
        print("K Number after sort: ", result)


#############    Result    ###############

# Test cases : 2
# Size : 6
# 0 : 7
# 1 : 10
# 2 : 4
# 3 : 3
# 4 : 20
# 5 : 15
# K : 3
# [3, 4, 7, 10, 15, 20]
# K Number after sort:  7
# Size : 5
# 0 : 7
# 1 : 10
# 2 : 4
# 3 : 20
# 4 : 15
# K : 4
# [4, 7, 10, 15, 20]
# K Number after sort:  15