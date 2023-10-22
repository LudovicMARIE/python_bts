from unicodedata import numeric


MAT=[[1,2,3],[4,5,6],[7,8,9]]
def ecrire_matrice(MAT):
    for carac in MAT:
        print(carac)
        if carac == "]":
            print("\n")

def luminosite(MAT):
    n=0
    avg = 0
    nbavg = 0
    for MAT[n] in MAT:
        for carac in MAT[n]:
            if carac <= 100 and carac >= 0:
                avg = avg+carac

    result = avg/(len(MAT)*len(MAT[0]))
    print(result)            

def contraste(MAT,lumin):
    n=0

    for MAT[n] in MAT:
        for carac in MAT[n]:
            if carac >=lumin:
                Ncarac=carac*2
                if Ncarac>100:
                    Ncarac = 100
            else:
                Ncarac = carac/2

    


    return



luminosite(MAT)

