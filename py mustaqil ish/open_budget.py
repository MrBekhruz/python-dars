# open budget dasturi tuziladi foydalanuvchi ism fammiliyasi vva telefon raqami olinadi 
# malumot jsonda saqlanadi , agar malumot jsonda bulsa unga siz avval ovoz bergansiz desin ,yangi foydalanuvchi bulsa
# biror kuchaga ovoz berib quyilsin
import json
import random
class Open:
    def __init__(self,ism,familiya,telefon_raqam,pasport,idcha,data):
        self.ism = ism
        self.familiya = familiya
        self.telefon_raqam = telefon_raqam
        self.pasport = pasport
        self.idcha = idcha
        self.data = data


    while True:
        def register(self):
            print('----------------------')
            print("----------Open budget dasturiga xush kelibsiz----------")
            self.ism = input("Assalom alaykum ismingizni kiriting: ").lower()
            self.familiya = input("Navbat endi familyaga, iltimos familiyangizni kiriting: ").lower()
            self.telefon_raqam = input("Iltimos telefon raqamingizni kirirting \nNAMUNA -> (+998)99-414-40-22: ")
            self.pasport = input('pasportseriya raqami: ')
            self.idcha = random.choice('123456879')
            for i in self.telefon_raqam:
                if i == '-':
                    continue
                print(i, end="")
        def append_data(self):
            malumot = []
            self.data = {
                'pasport':self.pasport,

                self.idcha :{
                'ism':self.ism,
                'familiya':self.familiya,
                'telefon_raqam':self.telefon_raqam,           
                }
            }
            malumot.append(self.data)
        # malumot = tuple(malumot)
        def main(self):
            if self.data['pasport'] == self.pasport :
                print('afsuski ruyhatdan utgansiz')
                break
            else:
                qishloq = ['Mitan','Arabsaroy','Qalqon Ota','Vomitan','Duldur','Qiziltepa','Armijon']
                print('--Qaysi qishloqqa ovoz berasiz?--')
                ovoz = input('>>> ')

                if ovoz in len(qishloq):
                    print("Saqlandi ")
                    self.data.update({'ovoz':ovoz})
                    json_file_name = 'data_file.json'
                    with open(json_file_name,'w') as json_f:
                        json.dump(malumot,json_f,indent=7)
                    print(f"json formatga saqlandi {json_f}")
                else:
                    print('Ovozni xato berdingiz')
        if __name__ == '__main__':
            