
def printPyramid(height, pramidType):

    for i in range(height):
        print((' '*(height-i-1))+(pramidType+' ')*(i+1))
    return None

if __name__ == "__main__":
    height = int(input("Enter Height Of Pyramid : ")) 
    pramidType = input("Symbol of Pyramid: ")

    printPyramid(height, pramidType)


######## Result ##########

# Enter Height Of Pyramid : 6
# Symbol of Pyramid: &
#      & 
#     & & 
#    & & & 
#   & & & & 
#  & & & & & 
# & & & & & & 


# Enter Height Of Pyramid : 3
# Symbol of Pyramid: ,
#   , 
#  , , 
# , , , 