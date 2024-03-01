# type casting = convert the date type of a value to another date type
a = 5 # int
b = 2.0 # float
c = '3' # str

a = int(a) 
b = int(b) # bu usul bilan biza float malumotni integrga uzgartirdik
c = int(c) # str metodini integrga uzgartirdik 

a = str(a) # int metodini str ga uzgartirdik
b = str(b) # float metodini str ga uzgartirdik
c = str(c)


a = float(a) # int  metodini float ga uzgartirdik
b = float(b)
c = float(c) # str metodini floatga uzgartirdik

print(a)
print(b)
print(c)


print(int(b))# bu udul bilan biza float malumotni integrga uzgartirdik
print(a * 3) # biza bu yerda uzgaruvchi qiynatini 3 ga kupaytirdik 
print(b * 3)   
print(c * 3) # agar biza str malumotni lyuboy songa kupaytirsak orqasidan usha sonnni ushancha marta kupaytirib beradi
print(c * 6) # example