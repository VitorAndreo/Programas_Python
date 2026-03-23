import pyautogui as posicao
import pygetwindow as gw

#Pressionando "windows" + "r" para abrir "Executar"
posicao.hotkey('win', 'r')

#Aguarda um tempo para o pc processar as informações
posicao.sleep(2)

#Digitando o comando para abrir o bloco de notas
posicao.typewrite('notepad')

#Aguarda um tempo para o pc processar as informações
posicao.sleep(2)

#Enter para executar o comando
posicao.press('enter')

#Aguarda um tempo para o pc processar as informações
posicao.sleep(5)

#Digitando algo no bloco de notas
posicao.typewrite('Abri o bloco de notas com python')

#Aguarda um tempo para o pc processar as informações
posicao.sleep(2)

#Fechando o bloco de notas
fecharNotepad = gw.getActiveWindow()

#Aguarda um tempo para o pc processar as informações
posicao.sleep(2)

#Fechar a janela ativa
fecharNotepad.close()

#Aguarda um tempo para o pc processar as informações
posicao.sleep(2)

#Pressionando tab para ir para o botão de não salvar
posicao.press('tab')

#Aguarda um tempo para o pc processar as informações
posicao.sleep(2)

#Confirmando com enter
posicao.press('enter')