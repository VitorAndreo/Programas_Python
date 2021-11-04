import random

def semente(numero, imprimirAte):
    print("\n----------")
    print("\nSemente inserida: ", numero)
    print("Número de pseudos: ", imprimirAte)
    aleatorio(numero, imprimirAte)

def aleatorio(numero, imprimirAte):
    repetido = set()
    cont = 0
    i = 0
    j = 0
    lista=[]

    while numero not in repetido:
        cont += 1
        repetido.add(numero)
        numero = int(str(numero * numero).zfill(8)[2:6])
        lista.append(numero)

    for i in range(imprimirAte):
        j += 1
        total = len(lista)
        aindaTemProximo = (i+1 < total)
        print("Valor #", j, ": ", lista[i])

        if aindaTemProximo:
            if(lista[i] == lista[i+1]):
                novaSemente = random.random()
                print("\nValor repetido! Nova semente = ", novaSemente,"\n")
                return aleatorio(novaSemente, imprimirAte)
        else:
            print("A Lista atingiu o limite em que chega com esta semente sem nenhuma repetição")
            break
                
                


    
numero = int(input("Coloque a semente: "))
imprimirAte = int(input("Coloque quantos números pseudoaleatórios você deseja ver: "))
semente(numero, imprimirAte)
