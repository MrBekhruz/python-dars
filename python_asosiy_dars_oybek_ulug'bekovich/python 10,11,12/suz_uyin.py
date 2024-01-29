# import random
# suzlar = ['python', 'kompyuter', 'uy', 'maktab', 'intellekt', 'kuprik', 'sarguzasht', 'talaba', 'mashina', 'ruchka', 'uyin']
# tanlangan_suz = random.choice(suzlar)
# tugri_javob = tanlangan_suz
# ishorali_suz = list("-" * len(tanlangan_suz))
# tugri_javob = list(tugri_javob)
# takrorlanish = True
# takrorlanishlar_soni = 0

# print("Salom o'yinga xush kelibsiz")
# print("Men bir so'z o'yladim va siz uni topishga harakat qiling")
# print("So'z", len(tanlangan_suz), "harfdan iborat")
# print("Sizda", len(tanlangan_suz), "* ta urinish mavjud")
# print("O'yin boshlandi")

# while takrorlanish:
#     taxmin = input("Taxminiy to'g'ri harfni kiriting: ").lower()

#     if len(taxmin) != 1 or not taxmin.isalpha():
#         print("Siz 2ta harf kirittiz yoki alfabetta mavjud emas harf")
#         continue

#     if taxmin in ishorali_suz:
#         print("Bizda bu harf allaqachon mavjud")
#         continue

#     takrorlanishlar_soni += 1

#     if taxmin in tugri_javob:
#         for indeks, harf in enumerate(tugri_javob):
#             if harf == taxmin:
#                 ishorali_suz[indeks] = taxmin
#         print("Urra tugri javob davom eting!")
#     else:
#         print("Notug'ri harf yana urinib kuring.")

#     print(" ".join(ishorali_suz))

#     if "".join(ishorali_suz) == tanlangan_suz:
#         takrorlanish = False
#         print("O'yiniiz tugaddi! To'g'ri javob: ", tanlangan_suz)
#         print("Harakatlar soni", takrorlanishlar_soni)