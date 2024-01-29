# a = 'va'

# b = a.center(50,'*')

# print(b)

# while True:
#     soat1 = int(input('1 soatni kiriting: '))
#     min1 = int(input('1 minutni kiriting: ' ))
#     secund1 = int(input('1 sceundni kiriting: '))

#     soat2 = int(input('2 soatni kiriting: '))
#     min2 = int(input('2 minutni kiriting: ' ))
#     secund2 = int(input('2 sceundni kiriting: '))
    
#     a = (soat2 - soat1) * 3600 + (min2 - min1) + (secund2 - secund1)
#     print('secund: {}'.format(a))

#     if soat1 > soat2:
#         break

#     else:
#         continue



# uch_xonali_son = int(input('iltimos uch xonali son kiriting (Misol: 685)'))
# a = int(input("uchxonali son kiriting: "))
# b = a % 10
# d = a // 100
# c = (a % 100 ) // 10
# f = b + d + c
# print ("Raqamlar yig'indisi: {} ga teng ".format (f))

# a=input("Son kiriting:")
# a=int(a)
# def yig(son):
#     a=len(str(son))
#     if a==1:
#         return son
#     elif a==2:
#         return (son%10)+(son//10)
#     elif a==3:
#         b=son%100
#         c=(b%10)+(b//10)
#         return c+(son//100)
# print('raqamlar tigindisi {}'.format(yig(a)))


from random import randint

a = randint(1,500)
b = randint(1,500)


c = int(input('{} + {} = '.format(a,b)))

if c == (a+b):
    print('tugri')

else:
    print('xato')