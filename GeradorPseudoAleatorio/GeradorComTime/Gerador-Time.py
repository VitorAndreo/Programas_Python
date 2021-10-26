import time

def semente(numero):
    print("Semente gerada: ", numero)
    aleatorio(numero)

def aleatorio(numero):
    repetido = set()
    cont = 0
    i = 0
    lista=[]

    while numero not in repetido:
        cont += 1
        repetido.add(numero)
        numero = int(str(numero * numero).zfill(8)[2:6])
        lista = (str(numero))
        print("Valor # ",cont, ": ",lista)
    

numero = time.time()


semente(numero)


