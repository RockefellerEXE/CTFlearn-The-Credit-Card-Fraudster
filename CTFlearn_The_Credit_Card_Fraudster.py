import re


findCard = "543210******1234"


pattern1 = "[0-9]+"  # NUBMERS
pattern2 = "\*+"  # only ****************************************
cardPrefix, cardSuffix = re.findall(pattern1, findCard)
missingNumbers = re.findall(pattern2, findCard).pop()
cards = []
x = 0

while x <= int("9"*len(missingNumbers)):
    check = cardPrefix+str(x).zfill(len(missingNumbers))+cardSuffix
    if int(check) % 123457 == 0:  # only multiple of 123457
        cards.append(check)
    x += 1
for card in cards:
    luhna = []
    control = []
    number = 0
    for x in card:
        luhna.append(x)
    control.append(int(luhna.pop()))
    for x in range(len(luhna)):
        if x % 2 == 0:
            luhna[x] = int(luhna[x])*2
            if int(luhna[x]) > 9:
                z = str(luhna[x])
                luhna[x] = int(z[0])+int(z[1])
        else:
            luhna[x] = int(luhna[x])*1
        number += luhna[x]
    if number % 10 != 0:
        if 10-number % 10 == control[0]:
            print("This is your flag:", "CTFlearn{"+card+"}")
