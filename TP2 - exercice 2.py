inputString = str(input("Please type a sentence: "))

count = 0;

for i in inputString:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count+=1
if count == 0:
    print('Pas de voyelle')
else:
    print('Le nombre de voyelle est : ' + str(count))