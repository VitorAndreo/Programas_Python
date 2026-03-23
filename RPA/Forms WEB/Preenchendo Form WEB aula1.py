from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import pyautogui as p
from selenium.webdriver.support.select import Select

navegador = wb.Chrome()

navegador.get('https://fom.jotform.com/221436066464051')

#Tempo para processar
p.sleep(2)

#Nome
navegador.find_element(By.NAME, 'q3_nome[first]').send_keys('Vítor')
p.sleep(1)

#Sobrenome
navegador.find_element(By.NAME, 'q3_nome[last]').send_keys('Andrêo')
p.sleep(1)

#Email
navegador.find_element(By.NAME, 'q4_email').send_keys('vitor@mail.com')
p.sleep(3)

#Pega o 2o item do dropdown "Estado Civil"
dropdown = navegador.find_element(By.ID, 'input_5')
selectedItem = Select(dropdown)
selectedItem.select_by_index(2)
p.sleep(2)

#Selecionando radio "Tem Filhos?"
filho = "Não"

if filho == "Sim":
    navegador.find_element(By.ID, 'label_input_6_0').click()
else:
    navegador.find_element(By.ID, 'label_input_6_1').click()
p.sleep(2)

#Marcando caixa de seleção "Cores favoritas (neste exemplo: azul e amarelo)
navegador.find_element(By.ID, 'label_input_7_0').click()
navegador.find_element(By.ID, 'label_input_7_1').click()
p.sleep(2)

#Marcando avaliação (nesse exemplo: 3 estrelas)
navegador.find_element(By.XPATH, '//*[@id="input_8"]/div[3]').click()
p.sleep(2)