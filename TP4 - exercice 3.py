def reduction(age):
    if (age <= 10):
        return 50
    elif (age >=11 and age <=18):
        return 30
    elif (age >=60):
        return 20
    else :
        return 0

def montant(tarif,age):
    promo = reduction(age)
    nTarif = tarif - (tarif*promo/100)
    return nTarif

total = 0
for i in range(0,5):
    tarif = int(input("Entrez votre tarif : "))
    age = int(input("Entrez votre age : "))
    result = montant(tarif,age)
    total = total+result

print(total)
