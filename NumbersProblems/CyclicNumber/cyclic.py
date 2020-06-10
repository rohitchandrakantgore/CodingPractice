
number = int(input('enter number : '))
count = 0
for i in range(1,7):
    numberMul = number*i
    # print(numberMul)
    if(sorted(list(str(numberMul)))==sorted(list(str(number)))):
        count+=1

if(count==6):
    print("It's A Cyclic Number.!")
else:
    print("It's not a Cyclic Number.")