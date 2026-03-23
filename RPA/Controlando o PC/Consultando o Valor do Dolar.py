import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#Tempo de espera para q o pc possa "pensar" ou processar as informações
tempoEspera.sleep(5)

#Movendo o mouse até o botão iniciar
posicaoMouse.moveTo(x=530, y=1055)

#Tempo de espera para q o pc possa "pensar" ou processar as informações
tempoEspera.sleep(2)

#Clicando na posicao
posicaoMouse.click(x=530, y=1055)

#Tempo de espera para q o pc possa "pensar" ou processar as informações
tempoEspera.sleep(2)

#Escrevendo a palavra "calc" para pesquisar calculadora
posicaoMouse.typewrite('google')

#Tempo de espera para q o pc possa "pensar" ou processar as informações
tempoEspera.sleep(2)

#Pressionando a tecla enter para abrir o google
posicaoMouse.press('enter')

#Tempo de espera para q o pc possa "pensar" ou processar as informações
tempoEspera.sleep(2)

#Movendo o mouse
posicaoMouse.moveTo(x=1065, y=607)

#Tempo de espera para q o pc possa "pensar" ou processar as informações
tempoEspera.sleep(2)

#Clicando na posicao
posicaoMouse.click(x=1065, y=607)

#Tempo de espera para q o pc possa "pensar" ou processar as informações
tempoEspera.sleep(5)

#Escrevendo a palavra "calc" para pesquisar calculadora
posicaoMouse.typewrite('Dolar hoje')

tempoEspera.sleep(2)

#Pressionando enter para realizar a pesquisa no navegador
posicaoMouse.press('enter')

print(posicaoMouse.position())