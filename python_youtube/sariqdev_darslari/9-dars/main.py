# # # 08-dars 
# # # Daturlash asoslari
# # # FOR LOOP
# # # Sana: 25/01/2024

mehmonlar = ['ali','vali','bexrux','john','kate','javohir']
for mehmon in mehmonlar:
    print('salom',mehmon)

mehmonlar =['ali','vali','bexrux','john','kate','javohir']
for mehmon in mehmonlar:
    print(f"Salom {mehmon}, sizni palonchi kuni nahorga chaqiramiz \n")
    print(f"Hurmat bilan palonchiyevlar \n")

sonalr  = list(range(1,10))
for son in sonalr:
    print(f"{son} ning kvadrati {son**2} ga teng")

sonlar = list(range(11))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar)
print(sonlar_kvadrati)

dustlar = []
print("5 ta eng yaqin dustingiznig ismi")
for n in range(5):
    dustlar.append(input(f"{n+1}-dustingizni ismi: "))
print(dustlar)



# mevalar = ['olam ', 'banan','limon', 'mandarin']
# for meva in mevalar:
#     mevalar.insert(2,'gullar')
#     print(meva)

while True:
    x = list(range(0,15))
    print(x)
    suz = int(input('index topamiz: '))
    if suz == x:
        for i in x:
            print(f"index quyidagicha {x.index()}")
    else:
        print('dastur tuxtadi')
        break

yangi_sonlar = [1,2,3,4,5,6,7,8,9,10]
for x in yangi_sonlar:
    search = int(input('namani qidirasiz: '))
    if search == yangi_sonlar.index(2):
        print(yangi_sonlar.index(2))


print(yangi_sonlar)
yangi_sonlar = tuple(yangi_sonlar)
search = int(input('amalni kirit 1 , 2 , 3'))
if search == 1:
    print(yangi_sonlar)
elif search == 2:
    print(f"malumot qushamiz")
else:
    print('error')
yangi_sonlar.append(search)

sonlar = list(range(0,11))
print(sonlar)
indexcha = int(input('qaysini indexi kerak: '))
if sonlar in indexcha:
    print(f"sonnning indexi  {sonlar.index(1,2,3,4,5,6,7,8,9,10)}")
# x = indexcha.index()
# print(x)
else:
    print('error')