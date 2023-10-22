L=[]
for i in range (10):
    nombre = int(input("Nombre : "))
    if i <3:
        L.append(nombre)
    elif i <6:
        for i in range (2):
            L.append(nombre)
    else: 
        for i in range (4):
            L.append(nombre)
    i = i+1

for x in range(len(L)):
    print (L[x])
moyenne = 0 
for k in range (len(L)):
    moyenne = moyenne + L[k]
moyenne = moyenne/25
print ("Moyenne :",moyenne)