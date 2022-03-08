
cardPrefix ="543210"
# nieznane gwiazdki :D ******
cardSuffix ="1234"
cards=[]
x=0
while x<=999999:
    check=cardPrefix+str(x).zfill(6)+cardSuffix
    if int(check)%123457==0:
        cards.append(check)
    x+=1
for card in cards:
    luhna=[]
    control=[]
    number=0
    for x in card:
        luhna.append(x)
    control.append(int(luhna.pop()))
    for x in range(len(luhna)):
        if x%2==0:
            luhna[x]=int(luhna[x])*2
            if int(luhna[x])>9:
                z=str(luhna[x])
                luhna[x]=int(z[0])+int(z[1])
                
        else:
            luhna[x]=int(luhna[x])*1
        number+=luhna[x]
    if number%10!=0:
        if 10-number%10==control[0]:
            print("CTFlearn{"+card+"}")

