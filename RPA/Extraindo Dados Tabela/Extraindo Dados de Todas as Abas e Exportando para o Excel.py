from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui as tempo
import pandas as pd

navegador = opcoesSelenium.Chrome()

#Abrindo o site do rpachallengeocr
navegador.get("https://rpachallengeocr.azurewebsites.net/")

listaDataFrame = []

linha = 1

i = 1

while i < 4:
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
    colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

    for linhaAtual in linhas:
        print(linhaAtual.text)
        listaDataFrame.append(linhaAtual.text)

        linha += 1


    i += 1

    #Para dar tempo do pc processar as infos
    tempo.sleep(2)

    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()

    # Para dar tempo do pc processar as infos
    tempo.sleep(2)

else:
    print("Concluído!")

arquivoExcel = pd.ExcelWriter('DadosAbasSite.xlsx', engine='xlsxwriter')
arquivoExcel._save()

dataFrame = pd.DataFrame(listaDataFrame, columns=['#;ID;Due Date'])

arquivoExcel = pd.ExcelWriter('DadosAbasSite.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel,sheet_name='Dados',index=False)

arquivoExcel._save()