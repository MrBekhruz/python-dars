# 08-dars 
# O'zgaruvchilar = variables
# Listlar(Ro'yhatlar bilan ishlash)
# Sana: 25/01/2024

cars = ['audi','bmw','chevrolet','kaptiva', 'genral']
cars.sort()
print(cars)

# Teskari tartib 
cars = ['audi','bmw','chevrolet','kaptiva', 'genral']
cars.sort(reverse=True)
print(cars)
# uzgaruvchining qiymatiga tegmagan holatda listni uzgartirish
cars = ['kaptiva','audi','genral','bmw','chevrolet']
print("sorted() qaytargan ruyxat :" , sorted(cars))
# teskari ruyxatni tartiblashda
print("sorted() qaytargan ruyxat :" , sorted(cars, reverse=True)) 
# listdagi joyini almashtirish
cars = ['kaptiva','audi','genral','bmw','chevrolet']
cars.reverse()
print(cars)
# listdagi uzunlikni topish uchun
cars = ['kaptiva','audi','genral','bmw','chevrolet']
print(len(cars))
# range funksiyasi
sonalr = list(range(0,11))
print(sonalr)
# /qadam berish uchun juft yoki toq
toq_sonlar = list(range(1,10,2))
# max qiymat uchun
max_qiymat = max(toq_sonlar)
# min qiymat uchun
min_qiymat = min(toq_sonlar)
# sum - yigindini hisoblash
sum_qiymat = sum(toq_sonlar)
print(sum_qiymat)
print(min_qiymat)
print(max_qiymat)
print("max qiymat: ", max_qiymat , " " "min qiymat: " , min_qiymat, " " 'sum_qiymat: ' ,sum_qiymat)

# RUYXATNI KESISH
cars = ['audi','bmw','chevrolet','kaptiva', 'genral']
print(cars[0:5])
print(cars[4:5])
print(cars[1:])
print(cars[:5])
# nusxa olish uchun [:]

my_cars = cars[:]
my_cars.append('GENTRA')
print(my_cars)

# TUPLE - UZGARMAS RUYXAT
#  tupleda hech qanday qiymatni uzgartirib bulmaydi, unga hech qanday append metodi ishlamaydi chunki uzgarmas
cars = ('audi','bmw','chevrolet','kaptiva', 'genral')
# # ERROR
# cars[2] = 'teddy'
# print(cars)
  
# uzgartirish kiritish uchhun tupleni -> listga aylantiramiz,keyin bemalolo apeend qilishimiz mumkin
cars = list(cars)
print(type(cars))
# listdan -> tuole utish uchun tuple funksiyasi dan foydalanamiz
cars = tuple(cars)
print(type(cars))