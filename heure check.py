X = int(input('Entrez 4 nombres à la suite'))
Y = int(input(''))
Z = int(input(''))
T = int(input(''))
if X >=10 or Y >=10 or Z >=10 or T >=10 : 
    print(X,Y,'h',Z,T,' pas valide')
else:
    if X >= 3:
        print(X+Y+'h'+Z+T+' pas valide')
    elif X == 2:
        if Y >= 5:
            print(X+Y+'h'+Z+T+' pas valide')
    elif Z >= 6 :
        print(X+Y+'h'+Z+T+' pas valide')
    elif T >= 6 :
        print(X+Y+'h'+Z+T+' pas valide')


