import random

dé = random.randrange(1,6)
listeDé=[]

tortueFin = int(input("Entrez les cases de la tortue"))
tortuePlace = 0
while tortueFin > tortuePlace : 
    if dé == 6 :
        listeDé.append(dé)
        print("le lièvre a gagné")
        for i in range (len(listeDé)):
            print(listeDé[i])
        
    elif tortueFin > tortuePlace: 
        listeDé.append(dé)
        print("La tortue avance")
        tortuePlace = tortuePlace + 1
        dé = random.randrange(1,6)
    else : 
        listeDé.append(dé)
        print("La tortue a gagné")
        for i in range (len(listeDé)):
            print(listeDé[i])


