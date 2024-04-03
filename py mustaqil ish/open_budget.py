import json
import random

class OpenBudget:
    def __init__(self):
        self.data = {}
    
    def register(self):
        print("----------Open budget dasturiga xush kelibsiz----------")
        ism = input("Assalom alaykum ismingizni kiriting: ").lower()
        familiya = input("Navbat endi familyaga, iltimos familiyangizni kiriting: ").lower()
        telefon_raqam = input("Iltimos telefon raqamingizni kirirting \nNAMUNA -> (+998)99-414-40-22: ")
        pasport = input('pasportseriya raqami: ')
        idcha = random.randint(100000, 999999)
        self.data[pasport] = {
            'ism': ism,
            'familiya': familiya,
            'telefon_raqam': telefon_raqam,
            'idcha': idcha
        }

    def main(self):
        with open('data_file.json', 'r') as json_file:
            try:
                existing_data = json.load(json_file)
            except json.JSONDecodeError:
                existing_data = {}
        
        self.data.update(existing_data)

        pasport = input('pasportseriya raqamingizni kiriting: ')
        if pasport in self.data:
            print('Afsuski, ruyhatdan utgansiz.')
        else:
            print('--Qaysi qishloqga ovoz berasiz?--')
            qishloq = ['Mitan', 'Arabsaroy', 'Qalqon Ota', 'Vomitan', 'Duldur', 'Qiziltepa', 'Armijon']
            ovoz = input('>>> ')
            if ovoz in qishloq:
                print("Saqlandi ")
                self.data[pasport]['ovoz'] = ovoz
                with open('data_file.json', 'w') as json_file:
                    json.dump(self.data, json_file, indent=4)
                print("Malumotlar JSON formatida saqlandi.")
            else:
                print('Ovozni xato berdingiz')

if __name__ == '__main__':
    budget = OpenBudget()
    budget.main()
