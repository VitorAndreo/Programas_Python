from docx import Document as Doc
from docx.shared import Pt
from openpyxl import load_workbook as lw
import os

nome_arquivo_alunos = "F:\\Python\\Word\\Alunos_.xlsx" #por estar na mesma pasta do código, não é necessário pegar caminho

planilhaDadosAlunos = lw(nome_arquivo_alunos)

#Selecionando a sheet/planilha/aba
sheet_selecionada = planilhaDadosAlunos['Nomes']

for linha in range(2, len(sheet_selecionada['A'])+1):
    #Abre o arquivo word
    arquivoWord = Doc("F:\\Python\\Word\\Certificado2.docx") #Pegar o template depois

    #Seleciona o estilo
    estilo = arquivoWord.styles["Normal"]

    #Pegando o nome do aluno quando passar na célula
    nomeAluno = sheet_selecionada['A%s' % linha].value

    for paragraph in arquivoWord.paragraphs:
        if "@nome" in paragraph.text:
            paragraph.text = nomeAluno
            fonte = estilo.font
            fonte.name = "Calibri (Corpo)"
            fonte.size = Pt(24)

    #Pegando o caminho da pasta e configurando o nome do certificado
    caminhoCertificados = "F:\\Python\\Word\\Certificados\\"+nomeAluno+".docx"

    #Salvando o certificado do aluno
    arquivoWord.save(caminhoCertificados)

print("Certificados gerados com sucesso!")