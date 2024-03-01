def main(minimum,maximum):
    son = []
    while minimum <= maximum:
        son.append(minimum)
        minimum +=1
    return son
print(main(0,71))