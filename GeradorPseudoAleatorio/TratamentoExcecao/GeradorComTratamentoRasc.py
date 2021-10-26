import time
import random
###
### Lista com tamanho grande (um milhão aproximadamente) travam o programada, não da erro, mas demora muito para dar resposta.
### Possivelmente está num loop infinito sem condição de parada.
###

def aleatorio(seed):
    numero=seed
    quadrado=numero*numero
    taux=len(str(quadrado))
    while taux<ndig*2:
        quadrado='0'+str(quadrado)
        taux=len(str(quadrado))
    numero=int(str(quadrado)[int(ndig/2):int(ndig/2+ndig)])
    i=1
    #caso pegue 0 a esquerda, o número de dígito será menor, então pego um número a mais na direita
    while len(str(numero))<ndig:
        numero=int(str(quadrado)[int(ndig/2):int(ndig/2+ndig+i)])
        i=i+1
    return numero

def semente():
    pseudo = random.randint(1, 1000000)
    aleatorio(pseudo)

#seed=int(input("digite a semente: "))
#seed=semente()
qtd=int(input("digite quantos números quer gerar: "))
ndig=len(str(semente)) 

semente()
lista=[]
i=0
while i<qtd:
    pseudo=(aleatorio(semente))
    lista.append(semente)
    i=i+1
print(lista)