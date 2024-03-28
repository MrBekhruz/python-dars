# open budget dasturi tuziladi foydalanuvchi ism fammiliyasi vva telefon raqami olinadi 
# malumot jsonda saqlanadi , agar malumot jsonda bulsa unga siz avval ovoz bergansiz desin ,yangi foydalanuvchi bulsa
# biror kuchaga ovoz berib quyilsin
import json
import random
def open_budget():
    malumot = []
    while True:
        print('----------------------')
        print("----------Open budget dasturiga xush kelibsiz----------")
        ism = input("Assalom alaykum ismingizni kiriting: ").lower()
        familiya = input("Navbat endi familyaga, iltimos familiyangizni kiriting: ").lower()
        telefon_raqam = input("Iltimos telefon raqamingizni kirirting \nNAMUNA -> (+998-99-414-40-22):")
        pasport = input('pasportseriya raqami: ')
        id = random.choice('123456879')
        for i in telefon_raqam:
            if i == '-':
                continue
            print(i, end="")
        data = {
            'pasport':pasport,

            id :{
            'ism':ism,
            'familiya':familiya,
            'telefon_raqam':telefon_raqam,           
            }
        }
        malumot.append(data)
        # malumot = tuple(malumot)
        if data['pasport'] == pasport :
            print('afsuski ruyhatdan utgansiz')
            break
        else:
            qishloq = ['Mitan','Arabsaroy','Qalqon Ota','Vomitan','Duldur','Qiziltepa','Armijon']
            print('--Qaysi qishloqqa ovoz berasiz?--')
            ovoz = input('>>> ')

            if ovoz in len(qishloq):
                print("Saqlandi ")
                json_file_name = 'data_file.json'
                with open(json_file_name,'w') as json_f:
                    json.dump(malumot,json_f,indent=7)
                print(f"json formatga saqlandi {json_f}")
            else:
                print('Ovozni xato berdingiz')
open_budget()
            

    