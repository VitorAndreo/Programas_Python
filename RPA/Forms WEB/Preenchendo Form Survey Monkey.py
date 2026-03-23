from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pyautogui as p
from selenium.webdriver.support.select import Select

navegador = wd.Chrome()

navegador.get('https://pt.surveymonkey.com/r/7GX9XRZ')

#Espera
p.sleep(5)

#Inserindo nome
navegador.find_element(By.NAME, '72542598').send_keys("Vítor Andrêo")
p.sleep(2)

#Inserindo email
navegador.find_element(By.NAME, '72542821').send_keys("vitor@mail.com")
p.sleep(2)

#Marcando a opção Masculino
navegador.find_element(By.XPATH, '//*[@id="583517054"]').click()
p.sleep(2)

