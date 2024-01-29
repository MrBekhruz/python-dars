        # 1 dastur
#yoshni hisoblaydigan dastur
# while True:
#     birth_year = input("enter your birth year")
#     age = 2023 - int(birth_year)
#     print(age)



            # 2 dastur
# kalkulyator
# first = float(input("first number: "))
# second = float(input("second number: "))
# sum = first + second
# print('natija : ' + str(sum))


            # pythonda boshlangich tushunchalar
# pythonda upper  lower find replace  in tushunchalar
    


            # 3 dastur
# suzlar = 'Python for beginners'
# print(suzlar.upper()) # suzlarni katta harfda yish ucun 
# print(suzlar.lower()) # suzlarni kichik harfda yozish uchun
# print(suzlar)
# print(suzlar.find('y')) # suzlarni ichida y harfi nechinchi indexda turibda aniqlash uchun ishlatilinadi
# print(suzlar.replace('for','man')) # pythonda berilgan replacedagi suz bilan yozmoqchi bulgan suz ''- ichida yoziladi va joyi almashadi
# print('Python' in suzlar) # bu malumot turi booloen malumot turi bulib yozgan uzgarruvchidan ichidan topib berish vazifasi


            # 4 dastur
# boolen malumotlar haqida gaplashamiz
# >,<,>=,<=,!= haqida gaplshamiz va nad 
# price = 25
# print(price > 10 and price < 30) # True
# print(price > 10 or price<30)
# print(not price > 10)
# --and-- ning vazifasi malumotni --True-- qilish uchun bergan malumotni ikkalsi ham tugri bulishi kerak
# --or-- ning vazifasi bergan malumotni kamida bittasi tugri bulishi kerak 
# --not-- vazifasi ikkalsi ham tugri bulmasligi kerak



            # 5 dastur
# if , elif, else shart tushunchalari
# komentariyani bitta lab ochib ishalatilsin
# dastur bittalab komentariyadan ochilib ishlatilsin
# temperatura = 25 # temperaturaga shartda berilgan raqamlarga qarab usish tartibida raqam berilsin
# if temperatura > 30:
#     print("it's a hot day")
#     print("drink plenty of water")

# elif temperatura > 20: # (20,30]
#     print("It's anice day")

# elif temperatura >10: #(10,20]
#     print("it's a bit cold")

# else:
#     print("it's a cold")

# print("done")



    # 6 dastur 
    # ogirlikni ulchaydigan dastur tuzamiz
# while True:
#     weight = float(input("weight: "))
#     unit = input("(K)g or (L)bs :")
    
#     if unit.upper() == 'K':
#         coverted = weight / 0.45
#         print("Weight in Lbs: " + str(coverted))
    
#     else:
#         coverted = weight * 0.45
#         print("Weight in Kgs:  " + str(coverted))



        # 7 datur
# while haqida

# i = 1
# while i <= 10:
#     i = i +1
#     print(i * '*')
 #ikkinchi qismni komentdan chiqarib ishlatilsin
# i = 1
# while i <= 10:
#     print(i)
#     i = i +1
  
        # 8 dastur
# lists haqida malumot.
# yangi malumot
# names = ['behruz','javohir','shahruz','dilshod','sarvar','javohir']
# names [2] = 'shashon' # malumot hato ketgan bulsa uni tuzatish uchun list nomi chaqirilinadi va listdagi qaysi malumpotni uzgartirish kiritish kerak bulsa uning index si chaqirilib olinadi
# print(names)
# print(names[0;3])

#list metodlari dastur davomi
#append , insert, remove,clear
# num = [1,2,3,4,5,6,7,8,9]
# num.append(11) # -- apppend metodining vazifasi malumotni listning oxiriga qushish
# num.insert(5,-1) # insert ni vazifasi shundan iboratki birinchi qaysi sondan keyin qanaqa malumot kelsin deb kod biz suraydi biz birinchi tanlangan sonni yozamizz keyin yozmoqchi bulgan sonni
# num.remove(5) # removeni vazifasi shundan iboratki qaysi sonnui uchirib yuborish kerakligi suraldiyani listdan malumotni uchirib yubotish
# num.clear() # bu metodni vazifasi shundan iboratki qavs ichida hech narsa bulmaydi list kursatilinadi usha listdan malumot uchirib tashlanadi
# print(1 in num) # bu bulen malumot turi bulib 1 raqam listdagi raqamlar ichida bor degani
# print(len(num)) # len vazifasi shundan iboratki listning nechta indexdan yani uzunliginio hisoblab  beradi
# print(num)
    # listlarning davomi
# listlarda --loop-- ning vazifasi\\
# num = [1,2,3,4,5,6,7,8]
# for a in num:
#     print(a)

# i = 0 # bu yerda 0 yozish uta muhim chunkiagar biz manfiy son yozadigan bulsak oxridagi indexdan yana sanashni boshlaydi biza 0 quyadigan bulsak yana qayta 0 indexdan sanaydi
# while i < len(num):
#     print(num[i])
#     i = i + 2 # bu yerda i ning vazifasi shundan iboratkio keyingi qayta dastur listni sanb yotgan payt biza qanaqa sonni yozsak ushancha tashab sanaydi agarda biza + dan keyin bir raqamini yozadigan bulsak listdahi malumotlarni qayta shu holicha sanaydi


        # 9 datur
# -- for -- haqida sanash
# numbers = range(5,10,2)
# for number in numbers: # bu dasturning asosiy maqsadi shundan iboratki rqamlarni ikkitadan tashlab uqish
#     print(number)
# for num in range(10): # buning asosiy vazifasi sonlarni 10 gacha sanash
#     print(num) 


        # thank you