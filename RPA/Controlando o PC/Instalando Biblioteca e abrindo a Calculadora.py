import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#Tempo de espera para q o pc possa "pensar" ou processar as informações
tempoEspera.sleep(5)

#Movendo o mouse até o botão iniciar
posicaoMouse.moveTo(x=584, y=1055)

#Tempo de espera para q o pc possa "pensar" ou processar as informações
tempoEspera.sleep(2)

#Clicando na posicao
posicaoMouse.click(x=584, y=1055)

#Tempo de espera para q o pc possa "pensar" ou processar as informações
tempoEspera.sleep(2)

#Escrevendo a palavra "calc" para pesquisar calculadora
posicaoMouse.typewrite('calc')

#Tempo de espera para q o pc possa "pensar" ou processar as informações
tempoEspera.sleep(5)

#Movendo o mouse até o botão iniciar
posicaoMouse.moveTo(x=653, y=340)

#Tempo de espera para q o pc possa "pensar" ou processar as informações
tempoEspera.sleep(2)

#Clicando na calculadora
posicaoMouse.click(x=653, y=340)

print(posicaoMouse.position())