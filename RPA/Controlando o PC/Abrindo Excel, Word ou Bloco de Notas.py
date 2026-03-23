import pyautogui as escolha

opcao = escolha.confirm('Clique no botao desejado',
                        buttons =['Excel', 'Word', 'Notepad'])
#Abrindo excel
if opcao == 'Excel':
    escolha.hotkey('win','r')
    escolha.sleep(2)
    escolha.typewrite('Excel')
    escolha.sleep(2)
    escolha.press('enter')
    escolha.sleep(2)
    escolha.moveTo(x=576, y=494)
    escolha.sleep(2)
    #Clicando em novo arquivo excel
    escolha.click(x=576, y=494)
    escolha.sleep(3)
    #Digitando no excel
    escolha.typewrite('Escolhi o excel')
    print('Voce escolheu abrir o Excel')

#Abrindo Word
elif opcao == 'Word':
    escolha.hotkey('win', 'r')
    escolha.sleep(2)
    escolha.typewrite('winword')
    escolha.sleep(2)
    escolha.press('enter')
    escolha.sleep(2)
    print(escolha.position())
    escolha.moveTo(x=425, y=315)
    escolha.sleep(2)
    # Clicando em novo arquivo excel
    escolha.click(x=425, y=315)
    escolha.sleep(3)
    # Digitando no excel
    escolha.typewrite('Escolhi o word')
    print('Voce escolheu abrir o Word')

#Abrindo bloco de notas
else:
    escolha.hotkey('win', 'r')
    escolha.sleep(2)
    escolha.typewrite('Notepad')
    escolha.sleep(2)
    escolha.press('enter')
    escolha.sleep(2)
    escolha.typewrite('Escolhi o bloco de notas')
    print('Voce escolheu abrir o Notepad')