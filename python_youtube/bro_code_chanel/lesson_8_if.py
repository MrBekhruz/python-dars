age = int(input('how are old are you'))

if age >= 100:
    print("you are century tears old")
elif age >= 10:
    print("you are adult ")
elif age < 0:
    print("you havent born yet")
else:
    print('you are a child')

    # logical operators (and,or,not )


temp = int(input('enter a day temperature:  '))

if temp >= 0 and temp <= 30:
    print(' todat temperature is good')

else:
    print('it is cold')


temp = int(input('enter a day temperature:  '))


if not(temp < 0 or temp > 30):
    print('temperatura juda yomon')
    print('stary at home')

elif not(temp >= 0 and temp <= 30):
    print ((' todat temperature is good'))
    print('go outside')


else:
    print('it is cold')