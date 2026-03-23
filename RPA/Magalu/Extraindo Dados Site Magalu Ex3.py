from selenium import webdriver as wd
from selenium.webdriver.common.by import By
import pyautogui as op
import pyautogui as t
import pandas as pd

navegador = wd.Chrome()

#Preparando o site
navegador.get('https://www.magazineluiza.com.br/')

#Procura pelo campo ID e digita o nome do produto
navegador.find_element(By.ID, 'header-search-input').send_keys("geladeira")
t.sleep(2)

#Apertando enter para pesquisar o produtor
op.press('tab')
op.press('tab')
op.press('enter')

#Tempo para carregar a lista de produtos do site
t.sleep(10)

#Criando o dataframe que vai receber os dados
listaDataFrame = []

listaProdutos = navegador.find_elements(By.CLASS_NAME, 'fHAfdj')

for produto in listaProdutos:
    nomeProduto = ""
    precoProduto = ""
    urlProduto = ""

    if nomeProduto == "":
        try:
            nomeProduto = produto.find_element(By.CLASS_NAME,'bohfAy').text
        except Exception:
            pass
    elif nomeProduto == "":
        try:
            nomeProduto = produto.find_element(By.CLASS_NAME, 'sc-ksCcjW').text
        except Exception:
            pass


    #-------------------------

    if precoProduto == "":
        try:
            precoProduto = produto.find_element(By.CLASS_NAME,'fATncB').text
        except Exception:
            pass
    elif precoProduto == "":
        try:
            precoProduto = produto.find_element(By.CLASS_NAME,'sc-cezyBN').text
        except Exception:
            pass
    elif precoProduto == "":
        try:
            precoProduto = produto.find_element(By.CLASS_NAME,'lmAmKF').text
        except Exception:
            pass
    elif precoProduto == "":
        try:
            precoProduto = produto.find_element(By.CLASS_NAME,'sc-dcJsrY').text
        except Exception:
            pass
    else:
        precoProduto = "0"

    # -------------------------

    if urlProduto == "":
        try:
            urlProduto = produto.find_element(By.TAG_NAME, 'a').get_attribute('href')
        except Exception:
            pass

    else:
        urlProduto = "-"

    print(nomeProduto,"-",precoProduto)
    print(urlProduto)

    dadosLinha = nomeProduto + ";" + precoProduto + ";" + urlProduto

    #Populando o Data Frame com as informações
    listaDataFrame.append(dadosLinha)

    arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')
    arquivoExcel._save()

    dataFrame = pd.DataFrame(listaDataFrame, columns=['Descrição;Preço;Url'])

    arquivoExcel = pd.ExcelWriter('dadosMagalu.xlsx', engine='xlsxwriter')

    dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

    arquivoExcel._save()