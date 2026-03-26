import requests as rq
import pandas as pd
import streamlit as st

def obter_request(url, params=None):
    """Faz uma requisiçã GET e retorna a resposta em JSON"""
    try:
        response = rq.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    except rq.HTTPError as e:
        print(f'Erro no request: {e}')
        return None
    
def frequencia_nome(name):
    """Obtém um dicionário de frequência de um nome por estado 
    no formato {década: quantidade}"""
    url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{name}'
    dados_nome = obter_request(url) or []
    #return {dados["periodo"]: dados["frequencia"] 
    #        for dados in dados_nome[0].get("res", [])}
    dados_dict = {dados["periodo"]: dados["frequencia"] 
            for dados in dados_nome[0].get("res", [])}
    df = pd.DataFrame.from_dict(dados_dict, orient="index")
    return df

def main():
    st.title("Web App API")
    st.header("Dados da API IBGE")
    in_name = st.text_input("Digite um nome: ")
    if not in_name:
        st.stop()
    df = frequencia_nome(in_name)
    col_1, col_2 =st.columns([0.3, 0.7])
    
    with col_1:
        st.write("Frequência por década")
        st.dataframe(df)
    with col_2:
        st.write("Série temporal")
        st.line_chart(df)
        
    #print(frequencia_nome(in_name))

if __name__ == "__main__":
    main()