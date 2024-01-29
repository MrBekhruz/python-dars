# 06-dars 
# O'zgaruvchilar = variables
# SONLAR BILAN ISHLASH
# INTEGR(int), FLOAT(float) Malumot turlari
# Sana: 25/01/2024
# Muallif: Baxtiyorov Behruz

#  print(type()) - ning vazifasi bizga malumotning turini aniqlab beradi
a = 20 # (int) butun son(natural son)
b = 5.5 #(float) o'nlik son kasr son
temp = 36.6
print(type(temp))
print(type(a))
print(type(b))

# agarda yozmoqchi bulgan soningiz juda ham katta buladigan bulsa uni pastki chiziq bilan yozing
aholi_soni = 8_594_376_467
print("Bugungi kunda: ",aholi_soni ," aholi soni" ) # int malumot bulganligi uchun --,-- vergul bilan ajratib yozamiz
print(type(aholi_soni))

# bir nechta uzgaruvchiga bitta qatorda qiymat berish
x,y,z = 5,5.2,6
print(x,y,z)

# PI constanta(uzgarmas qiymat) pythonda uzgarmas qiymatlarni katta harflar bilan yozish natijasida erishiladi
# Masala:
# aylananing uzunligini top radius = 20
radius = 20
diametr = 2 *radius
PI = 3.14
print("Aylana uzunligi: ", PI*diametr)

# (str) malumotlarni tugridan tugri (int) malumotlarga qushib chiqara olmaymiz
ism = "Bexruz"
yosh = 16
output = ism + ' ' + str(yosh) + ' ' + 'yoshda'
print(output)

# Masala:
# uzgaruvchidan tugilgan yilini kiritishini suraymiz uning yoshini hisoblash
# agarda siz foydalanuvchida son kiritishini surasangiz avval (int) sung (input) qilib masaladan namuna kurib yozing
t_yil = int(input('Tugilgan yilingizni kiriting: '))
current =  2024 - t_yil
print("Siz ",current,"yoshda ekansiz")