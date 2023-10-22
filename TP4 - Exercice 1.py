def val2(nombre):
    puissance = 0
    diviseurs=[]
    while (2**puissance <nombre):
        puissance=puissance+1
    for j in range(0,puissance):
        if (nombre%(2**j)==0):
            diviseurs.append(j)
    return max(diviseurs)

input = int(input("Entrez un nombre : "))
result = val2(input)
print(result)