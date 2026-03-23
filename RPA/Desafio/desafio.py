import pyautogui as pyauto
from selenium import webdriver as wd
from selenium.webdriver.common.by import By

navegador = wd.Chrome()

navegador.get('https://rpachallenge.com/')

#Tempo para processar
pyauto.sleep(2)

#Para usar o ng-reflect, devemos colocar o valor entre /*[@] para o python entender (bom de usar ele é que nunca muda)
#First Name
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelFirstName"]').send_keys('Vítor')
pyauto.sleep(1)

#Last Name
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelLastName"]').send_keys('Andrêo')
pyauto.sleep(1)

#Email
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelEmail"]').send_keys('vitors@gmail.com')
pyauto.sleep(1)

#Address
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelAddress"]').send_keys('Rua ABC, 1030')
pyauto.sleep(1)

#Phone
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelPhone"]').send_keys(14987966359)
pyauto.sleep(1)

#Company Name
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelCompanyName"]').send_keys('DXC')
pyauto.sleep(1)

#Role in company
navegador.find_element(By.XPATH, '//*[@ng-reflect-name="labelRole"]').send_keys('Developer')
pyauto.sleep(1)

#Submit
navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()
pyauto.sleep(3)