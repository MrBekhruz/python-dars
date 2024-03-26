# slicing = create a substring by extrasting elements from another string
#            indexing[] or slice()
#            [start:stop:step]

name = 'bro codde'
print(len(name))

first_name = name[0]
last_name = name[4:9]
funky_name = name[0:4:9]
reversed_name = name[::-1]


print(funky_name)
print(first_name)
print(last_name)
print(reversed_name)


#         slice ulash websiteni ulash
website1 = 'http://google.com'
# print(len(website1))
website2 = 'http://wkipedia.com'
print(len(website2))
print(website1)
slice = slice(0,19)
print(website1[slice])
print(website2[slice])

name = "BexruzBaxtiyorov"
first_name = name[:7]
last_name = name[7:]
umumiy = first_name + last_name
print(umumiy)
funky_name = name[::2]
print(funky_name)
def websitecha():
    website = 'http://google.com'
    slicecha = slice(0,19)
    print(website[slicecha])
websitecha()