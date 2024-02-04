# 07-dars 
# O'zgaruvchilar = variables
# Listlar(Ro'yhatlar bilan ishlash)
# Sana: 25/01/2024
# Muallif: Baxtiyorov Behruz
# list = [],  tupl = (), dictionary = {} 
# LISTLARNI TUZAYOTGANIMIZADA DOIMO , VERGUL BILAN AJRATAMIZ AGAR QUSHAYOTGAN MALUMOTIMIZ str bulsa '' qushtirnoqlar ichida yozamiz

# pythonda listlarda sanoq 0 dan boshlandi print(mevalar[0])
# listni oxiridagi elementga murojaat qilmoqchi bulsak [-1] orqali qilinadi 
mevalar = ['olma','anor','o\'rik','anjir','shaftoli','anaconda']
sonlar = [1,2,3,4,5,6,7,8,9,10]
sonlar_mevalar = [1,2,3,4,5,6,7,8,9,10,'olma','anor','o\'rik','anjir','shaftoli','anaconda']
bush_list = []
print(mevalar[-1])
print("Birinchi meva: ",mevalar[0])
print("Ikinchi meva: ",mevalar[1])
print("Birinchi meva: ",mevalar[1].title())
print("Ikinchi meva: ",mevalar[1].upper())
print('uch soni: ',sonlar[1] + sonlar[0])


# append
# append qilib listga malumot qushadigan bulsak listning oxiriga malumot qushadi
mevalar = ['olma','anor','o\'rik','anjir','shaftoli','anaconda']
mevalar.append('lenovo')
print(mevalar)
sonlar = [1,2,3,4,5,6,7,8,9,10]
sonlar.append(25)
print(sonlar)


# insert
# insert ni vazifasi urniga almashtirish index yoziladi va nimaga uzgartirish verguldan sung yoziladi
cars = ['LACETTI','KAPTIVA','MALIBU','TRACKER']
cars.insert(0,'Malibu')
cars.insert(-1,'Cobalt')
print(cars)


# del
# delni vazifasi listdagi malumotni albatta index yozilgandan sung uchiriladi
cars = ['LACETTI','KAPTIVA','MALIBU','TRACKER']
del cars[2]
print(cars)

# remove
# removeni vazifasi shundan iborat ki sizda list mavjud uni bitta elementni uchirmoqchisiz lekin uni indexni bilmaysiz
cars = ['LACETTI','KAPTIVA','MALIBU','TRACKER']
cars.remove('LACETTI')
print(cars)

# pop 
# pop ni vazifasi ham uchirish fat ruyhatni oxiridan uchirish
cars = ['LACETTI','KAPTIVA','MALIBU','TRACKER']
cars.pop()
print(cars)


# praktik datur
bozorlik = ['un','banan','gusht','suv','sokcha','kalbasa','tuxum']
sotib_olindi = bozorlik.pop(3)
print("Men " + sotib_olindi + 'sotib olindi')
print('qoldi: ',bozorlik )