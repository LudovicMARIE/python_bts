inputChain = str(input("Please type a sentence: "))
inputCarac = str(input("Please type a caracter :"))
count=0;
if (len(inputCarac) >= 1):

    for i in inputChain:
        if i == inputCarac:
            count+=1
if count == 0:
    print('No caracter found')
else:
    print('Caracter found, there is : ' + str(count))