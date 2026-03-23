from docx import Document as Doc
from docx.shared import Pt

#Abre o arquivo word
arquivoWord = Doc("F:\\Python\\Word\\Certificado1.docx") #Pegar o template depois

#Seleciona o estilo
estilo = arquivoWord.styles["Normal"]

for paragraph in arquivoWord.paragraphs:
    if "@nome" in paragraph.text:
        paragraph.text = "Vítor Andrêo"
        fonte = estilo.font
        fonte.name = "Calibri (Corpo)"
        fonte.size = Pt(24)

#Salvando o certificado do aluno
arquivoWord.save("VitorAndreo.docx")