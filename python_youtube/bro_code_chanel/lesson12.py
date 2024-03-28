food = ["piza",'hamburger', 'cola']
food.append("Lstning oxiriga qushadi")
food.remove("piza") #---------listdagi aytilgan narsani uchiradi agar ;stda busa uchiradi
food.pop() # ----- remove last element in list
food.insert(0,"cake ,,,,, urniga almashtiradi") # ==== food[0] = 'cake'
food.sort(reverse=False) # ---- sartirovka chapacha qilib 
food.clear() # ---- hammasi uchadi
fooof1 = food.count('piza')
print(fooof1)

if "cola" in food:
    print('Cola is here')


# 2D LISTS = a list of lists
        
drinks = ['cola','soda','tea']
food = ['palov','soup','manti']
desert = ['cake','ice cream']
meals = (drinks,food,desert)
print(meals)
print(meals[0][0]) # ------ drinks listdagi nolinchi element



# touples = collection which is ordered and uncheagable
#           used to group together related data

touple = ("Bro",21,"male")
print(touple.count("Bro")) # ---- necha marta takrorlangani surash uchun
print(touple.index('male')) # --- indexni topish uchun

if 21 in touple:
    print(f"numbers is here {21}")


import time
# ermakka dasturcha navigation karusel
# import time
while True:
    for x in food:
        for i in range(2):
            time.sleep(1)
        print(x)



# sets = collection is unordered, un indexed, NO duplicate value

set1 = {'fork','kniwes','spoon'}
set2 = {'dish','palate'}
set1.add('napkin') 
set1.remove('fork')
set1.clear()
set1.update(set2)
# print(set1)
dinner_table = set1.union(set2) 
print(dinner_table)
print(set1.difference(set2)) # ikkalsida nima qayta takrorlanganligini kursa buladi
print(set1.intersection(set2)) # ikkalasida takror kelgan narsani kursatadi
for x in set1:
    print(x)