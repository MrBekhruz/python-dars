# 04-dars 
# O'zgaruvchilar = variables
# Malumot turlari
# Sana: 25/01/2024
# Muallif: Baxtiyorov Behruz

# # # # # # # # # # # # # # # # # # # #
# Malumot turlari to'rtta             #
# Bular:                              # 
#  STRING(str '') = HARFLAR BELGILAR  #
#  INTEGR(int) = NATURAL SONLAR       #
#  FLOAT(5.2) = BUTUN SONALAR         #
#  BOOLEN = TRUE, FALSE               #
# # # # # # # # # # # # # # # # # # # # 



# # # # # # # # # # # # # # # # # # # # # # # # # # #
# pythonda uzgaruvchini elon qilganda                 #  
# qiymatiga mos nom bering                              #
# uzgaruvchi = qiymat                                     #
# pythonning maxsus funksiyalari uzgaruvchi bula olmaydi  #
# def = Bexruz BU katta xato                            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # 1-usul
ism = 'Behruz'
yosh = 16
print(ism,yosh)

    #  2-usul
ism , yosh = 'Bexruz', 16
print(ism)
print(yosh)

# uzgaruvchi yaratganda doimo etiborli buling 
# uzgaruvchi ikkita yoki undan kup suzdan tashkil topgan bulsa hech qachon orasini ochiq qoldirmang uninig urniga _ pastki chiziq bilan bog'lang
# dasturchilar ayniqsa pythonda ishlaydiganlar snackcase juda ham yoq tirishadi 
# snackcase bu pastki chiziq  '_' 
familiya_ism_sharif = 'Baxtiyorov Bexruz Baxodirivich'
print(familiya_ism_sharif)

# Masala:
# To'g'ri to'rtburchakning perimetrini toping
# 1-usul
a = 12
b = 25
P = (a + b) * 2

print(P)

# 2-usul

a = 12
b = 25
P = (12 + 25) * 2
print(P)


# Kvadratga oshirish uchun ** ikki marta kupayturuv belgisi quyiladi

# Masala
# 5 ning kvadratini hisoblab ber

# 1-usul
a = 5 
print(a**2)

# 2-usul
a = 5 
b = a ** 2  # 5 ** 2 
print(b)