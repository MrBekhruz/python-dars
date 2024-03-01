# for loop = a statement that will execute it's black of code 
#           a limited amount of times


#              while loop = unlimited
#               for loop = limited

# for i in range(0,100+1,10): # +1 ning vazifasi shundan iboratki 10gacha sanash uni quymasask 9 gacha sanash  # verguldan sung hohlagan son quysak buladi sababi bu nechta tashab sanash 
#     print(i) 

# for i in range(10):
#     print(i + 1) # 1 dan boshlab sanash uchun i ga bir qushdik
    

for i in 'bro code':
    print(i)



import time

for i in range(10,0,-1): # buni vazifasi 10 dan 1 gacha sanash 0 hisobga olinmaydi bir bir ayirib
    print(i)
    time.sleep(3) # bu yerda sukund ifosalandi bir secunda chiqishini aytdik
print("HAppy new year")


# nested loops = the inner loop will finish all of it's interations before
# finishing one iterations of the outer loop

rows = int(input('how many rows: '))
columns = int(input('how many columns: '))
symbol = input('enter a symbol')

for i in range(rows):
    for i in range(columns):
        print(symbol, end="thi is")
    print()
