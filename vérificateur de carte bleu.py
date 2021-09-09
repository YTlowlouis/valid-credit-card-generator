import random
#print(random.randint(0,9))
#numeros = input("Saisir les 16 numéros (sans espace)")
for j in range(1000000):
    numeros = random.randint(0,9)
    numeros=str(numeros)
    for i in range(15):
        a=random.randint(0,9)
        a=str(a)
        numeros += a




    try:
        int(numeros)
    except ValueError:
        exit("La saisie n'est pas un nombre (sans espace) !")

    if len(numeros) != 16:
        exit("La saisie ne comporte pas 16 chiffres !")


    for k in range(0, 15, 2):

        numeroLuhn = str(int(numeros[k]) * 2)

        if len(numeroLuhn) == 2:

            numeroLuhn = str(int(numeroLuhn[0]) + int(numeroLuhn[1]))

        numeros = numeros[:k] + numeroLuhn + numeros[k + 1:]


    somme = 0
    for k in range(0, 16):
        somme += int(numeros[k])

    reste = somme % 10

    if reste == 0:
        print("La Carte Bleue est \"vérifiée\" !")
        print(numeros)
        with open('nomcarte', 'a') as f:
            f.write(numeros)
            f.write("\n")
    else:
        cle = int(numeros[15])

        print("Pour que la Carte Bleue soit vérifiée, il faut que la clé soit: "
            + str((cle - reste) % 10))