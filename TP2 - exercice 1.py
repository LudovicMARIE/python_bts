import random

nombre = random.randrange(1,100)

essai = int(input("Devinez le nombre"))
while essai != nombre:
    print ("Ce n'est pas le nombre mystère")
    if essai < nombre:
        print("Le nombre est plus grand")
    if essai > nombre:
        print("Le nombre est plus petit")
    
    essai = int(input("Devinez le nombre"))

print ("Bravo, le nombre était",nombre)
