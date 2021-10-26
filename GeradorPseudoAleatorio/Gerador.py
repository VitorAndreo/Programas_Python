def semente(numero):
    aleatorio(numero)

def aleatorio(numero):
    repetido = set()
    cont = 0
    i = 0
    lista=[]

    while numero not in repetido:
        cont += 1
        i += 1
        repetido.add(numero)
        numero = int(str(numero * numero).zfill(8)[2:6])
        lista = (str(numero))
        print("Valor # ",cont, ": ",lista)
    

numero = int(input("Entre com o valor da semente (número mínimo de dígitos recomendado: 3) :\n"))

semente(numero)


