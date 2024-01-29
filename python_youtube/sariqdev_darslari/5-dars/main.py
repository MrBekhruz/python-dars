# 05-dars 
# O'zgaruvchilar = variables
# INPUT
# STRING Malumot turlari
# Sana: 25/01/2024
# Muallif: Baxtiyorov Behruz

#  STRING MALUMOTLAR UCHTA(3) - ('', "", - bu ikkalasining manosi bir xil xoxlaganini ishlatsangiz buladi) ('''''', qatorni pastga tushirganda bushliqqacha hisobga oladi)
# !!! O'ZGARUVCHI DOIMO LOTIN ALIFBOSIDA BULISHI SHART - UNING ICHIDAGI QIYMAT XOHLAGAN TILDA BULISHI MUMKIN  !!!
# AGARDA UZGARUVCHI KATTA HARFLARDA YOZILSA BU QIYMATNI UZGARTIRIB BULMAYDI 
# CHUNKI PYTHON BUNI CONSTANTA - UZGARMAS QIYMAT DEB QABUL QILGAN

# ism = "Bexruz"
# familiya = 'Baxtiyorov'
# print(ism + familiya) # agarda ismdan sung bitta bushliq(probel) quyilmasa ikkita uzgaruvchini bir biriga yopishtirib quyadi

ism = 'Bexruz'
familiya = "Baxtiyorov"
print(ism + ' ' + familiya) # ' ' - buning manosi bitta bush joy quyib ber degani

# f"" F-STRING
# f"" HAR DOIM "" - QUSHTIRNOQLAR --f-- ga yopishib tursin va uning ichiga uzgaruvchi --{}-- jingalak qavslar yordamida chaqiriladi 
# print(print(f"{ism} {familiya}")) print funksiyasinig ichida ham yozsa buladi
ism = 'Bexruz'
familiya = "Baxtiyorov"
familiya_ism = f"{ism} {familiya}" 
print(familiya_ism)
# print(f"{ism} {familiya}")

ism = 'Bexruz'
familiya = "Baxtiyorov"
print(f"Salom mening ismim {ism}.Familiyam {familiya}.{ism} {familiya}")

print('Hello world!')
print('Hello \tworld!') # Uzun  joy  tashlab   beradi 
print('Hello \nworld!') # Qatorga bulish


# STRING METODLARI
# !!! STRING METODLARIDA o'zgaruvchidagi qiymat o'zgarmaydi faqat yozilish turi uzgaradi lekin siz buni uzgartirishingiz mumkin
# Masalan:
# ism = 'Bexruz'
# familiya = "Baxtiyorov"
# ism_familiya = f"{ism} {familiya}"
# ism_familiya = ism_familiya.upper()
# ism_familiya = f"{ism_familiya.title()}"
# print(ism_familiya)


# .upper() - O'ZGARUVCHIDAGI HAMMA HARFNI KATTA QILIB YOZIB BERADI
# .capitalize() - o'zgaruvchidagi faqat birinchi suzning birinchi harfni katta qilib yozib beradi
# .center() - o'zgaruvchining joylashuvini o'rtaga olib chiqarib beradi
# .lower() - o'zgaruvchidagi hamma qiymatni kichkina harfga olib beradi
# .title() - o'zgaruvchida berilgan qiymatlarning hamma suzini birinchi harfini katta qilib yozib beradi 
ism = 'Bexruz'
familiya = "Baxtiyorov"
ism_familiya = f"{ism} {familiya}"
print(ism_familiya.upper())
print(ism_familiya.capitalize())
print(ism_familiya.center)
print(ism_familiya.lower())
print(ism_familiya.title())



# .lstrip() - chap tomondagi bushliqni olib tashlaydi
# .rstrip() - o'ng tomondagi bushliqni olib tashlaydi
# .strip() -umumiy bushliqni olib tashlaydi
meva = '   mandarin   '
print(meva)
print('Men ' + meva.lstrip() + ' yeyishni yaxshi ko\'raman')
print('Men ' + meva.rstrip() + ' yeyishni yaxshi ko\'raman')
print('Men ' + meva.strip() + ' yeyishni yaxshi ko\'raman')
print('Men ' + meva + ' yeyishni yaxshi ko\'raman')


# INPUT
# input bu foydalanuvchidan(user) string malumot qabul qilamiz endi o'zgaruvchini o'zimiz qo'lda kiritmaymiz

name = input("Ismingiz nima?: ")
print("Assalom alaykum " + name)

name = input("Ismingiz nima? \n>>>: ")
print("Assalom alaykum " + name.title())