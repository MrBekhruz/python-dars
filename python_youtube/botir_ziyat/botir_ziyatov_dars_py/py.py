year = int(input('yilni kiriting'))
a = 0
a +=1
if year % 4 == 0:
    print('bu kabisa yili')

if year %400 == 0:
    print('kabisa yili')

if year %100 == a:
    print('bu kabisa yili emas')

else:
    print('xato')

import calendar
calendar.isleap(2020)

my = ['shoshon','bexa','java']

x = '-'.join(my)  
print(x)