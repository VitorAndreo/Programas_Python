import time

def semente(numero, imprimirAte):
    print("Semente inserida: ", numero)
    print("Número de pseudos: ", imprimirAte)
    aleatorio(numero, imprimirAte)

def aleatorio(numero, imprimirAte):
    repetido = set()
    cont = 0
    i = 0
    lista=[]

    while numero not in repetido:
        cont += 1
        repetido.add(numero)
        numero = int(str(numero * numero).zfill(8)[2:6])
        lista.append(numero)
        
        if(i < imprimirAte):
            print("Valor # ",cont, ": ",lista[i])
            i += 1
            
           

numero = int(input("Coloque a semente: "))
imprimirAte = int(input("Coloque quantos números pseudoaleatórios você deseja ver: "))
semente(numero, imprimirAte)