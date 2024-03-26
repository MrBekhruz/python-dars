# break - tuxtatish 
# continue - utkazish
# pass - tashlab ketish

# BREAK
while True:
    name = input("enter your name: ")
    if name != "": # yokida if len(name) == ""
        break # yokida print(name)


# CONTINUE
phone_namber = "123-456-789"
for i in phone_namber:
    if i == '-':
        continue
    print(i, end="")

# PASS
for i in range(20):
    if i == 13:
        pass

    print(i)


