
number = int(input('enter number : '))

ops = 0
intial=2
def checkOperations(number,ops, intial):
    while(number>0):
        if(number%2==0):
            intial = doubleNumber(intial)
            ops+=1
            number = number//2
        else:
            initial = addOne(intial)
            ops+=1
            number = number-1
    return ops

def addOne(number):
    return number+1

def doubleNumber(number):
    return number*2
print('Steps to reach : ',checkOperations(number,ops,intial))



######## Result ######
# enter number : 7
# Steps to reach :  5

# enter number : 8
# Steps to reach :  4