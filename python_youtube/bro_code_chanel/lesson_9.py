# while loop = a statement that will execute it's block of code,
            # as long as it's condition remains true


# name = ''

# while len(name) == 0:
#     name = input('enter your name ')

# print("Hello " + name)

name = None

while not name:
    name = input('enter your name ')

print("Hello " + name)