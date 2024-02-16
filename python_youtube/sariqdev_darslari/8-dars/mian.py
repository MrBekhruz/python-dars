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
print(min_qiymat)
print(max_qiymat)
print("max qiymat: ", max_qiymat , " " "min qiymat: " , min_qiymat)

