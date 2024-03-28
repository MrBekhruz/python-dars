#  ERMAK UCHUN INDEX TOPADIGANN DASTUR
listcha = ['meva','banan','olma','shirinlik']
print(listcha)
suroq = input("nimani indexi kerak: ")

if suroq in listcha:
    print(listcha.index(suroq)) 
else:
    print('tugri kiritganligizga ishonch hosil qiling')

# dictionary = A changeable unordered collection of uniqque key:value pairs
#              fast because they use hashing allow use to access a value quickly

capitals = {'USA':'Washington DC,',
            'India':'New Dehli',
            'China':'Beijing,',
            "Russia":' '}
print(capitals['Germany']) # ERROR
print(capitals.get('GERMANY')) # NONE QAYTARADI
print(capitals.keys()) # barcha kalit suzlarni chiqaradi birinchi tuplga utkazib kiyin listga utkazai
print(capitals.values()) # qiymatlarni chiqaradi
print(capitals.items()) # dictdan malumot olib chiqadi tupl ichiga listni ochib tuplga saqlaydi
print(capitals)
capitals = {'USA':'Washington DC,',
            'India':'New Dehli',
            'China':'Beijing,',
            "Russia":' '}
print(len(capitals))
suroq = input('qayerning poytaxti kerak: ')
suroq = capitals.keys()
if suroq == capitals.keys():
    suroq = capitals.get(capitals.values())
    print(suroq)
    print(capitals.get(suroq))
for suroq in capitals:
    print(capitals.get(capitals.values))
# for key,value in capitals.items():
#     print(key,value)


if capitals['Russia'] is  None:
    print(capitals)
else:
    print('russia is none')