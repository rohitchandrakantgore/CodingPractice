
inputString = list(input("Enter String : "))

vowels = ['a', 'e', 'i', 'o', 'u']
for i,j in enumerate(inputString):
    if j in vowels:
        inputString[i] = j.upper()
 
result = ''.join(inputString)
print('result : ', result)


###### Result #######

# Enter String : rohit mininath Akshay
# result :  rOhIt mInInAth AkshAy