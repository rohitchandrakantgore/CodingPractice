
number = input('enter Number : ')

def checkDuck(number):
    return True if number.startswith('0') else False


if(checkDuck(number)):
    print('its a duck number')
else:
    print('not a duck number')

