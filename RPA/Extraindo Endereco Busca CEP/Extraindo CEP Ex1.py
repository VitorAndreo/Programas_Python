from selenium import webdriver as wb
from selenium.webdriver.common.by import By
import pyautogui as p

navegador = wb.Chrome()
navegador.get("https://buscacep.com.br/")

#Tempo para processamento
p.sleep(3)

#Inserindo um cep na caixa de cep do site buscacep
navegador.find_element(By.NAME, "cep").send_keys("13321261")

#Tempo para processamento
p.sleep(2)

#Clica no botão de pesquisar
navegador.find_element(By.NAME, "submit").click()

#Tempo para processamento
p.sleep(5)

#--------------------------Obtendo informações do site pelo xpath------------------------------#
rua = navegador.find_element(By.XPATH, '/html/body/main/div/div/div[3]/div[2]/div[2]/div[1]/div/p').text
print("Rua:",rua)

bairro = navegador.find_element(By.XPATH, '/html/body/main/div/div/div[3]/div[2]/div[2]/div[3]/div/p').text
print("Bairro:",bairro)

cidade = navegador.find_element(By.XPATH, '/html/body/main/div/div/div[3]/div[2]/div[2]/div[4]/div/p').text
estado = navegador.find_element(By.XPATH, '/html/body/main/div/div/div[3]/div[2]/div[2]/div[5]/div/p').text
print("Cidade:",cidade,"-", estado)

cep = navegador.find_element(By.XPATH, '/html/body/main/div/div/div[3]/div[2]/div[1]/div/div/div/span').text
print("CEP:",cep)