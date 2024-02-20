# 08-dars 
# Daturlash asoslari
# FOR LOOP
# Sana: 25/01/2024

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