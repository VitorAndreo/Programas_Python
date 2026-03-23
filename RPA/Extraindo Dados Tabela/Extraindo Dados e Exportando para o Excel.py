from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pandas as pd

navegador = opcoesSelenium.Chrome()

#Abrindo o site do rpachallengeocr
navegador.get("https://rpachallengeocr.azurewebsites.net/")

elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

linhas = elementoTabela.find_elements(By.TAG_NAME, "tr")
colunas = elementoTabela.find_elements(By.TAG_NAME, "td")

dataFrameLista = []

linha = 1
for linhaAtual in linhas:
    print(linhaAtual.text)
    dataFrameLista.append(linhaAtual.text)
    linha = linha + 1

arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')
arquivoExcel._save()

dataFrame = pd.DataFrame(dataFrameLista, columns= ['Dados'])

#Prepara o arquivo do Excel usando xlsxwriter como mecanismo
arquivoExcel = pd.ExcelWriter('dados.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='Sheet1', index=True)

#Salva as infos no arquivo de excel
arquivoExcel._save()

arquivoExcel = pd.ExcelWriter('DadosAbasSite.xlsx', engine='xlsxwriter')
arquivoExcel._save()

dataFrame = pd.DataFrame(listaDataFrame, columns=['#;ID;Due Date'])

arquivoExcel = pd.ExcelWriter('DadosAbasSite.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel,sheet_name='Dados',index=False)

arquivoExcel._save()