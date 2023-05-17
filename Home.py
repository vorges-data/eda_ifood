# Libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


st.set_page_config(page_title='Home', page_icon= '📊')

image = Image.open('Logo Preto Sem Fundo.png')
st.sidebar.image( image, width = 120)

st.sidebar.markdown('# Ifood Dataset')
st.sidebar.markdown("""---""")
st.sidebar.write('Faça o Download dos dados aqui:')

#===================================== Botão de Download ====================
data_download = pd.read_csv('dataset/mkt_data.csv')

st.sidebar.download_button(
        label = 'Download',
        data = data_download.to_csv( index=False, sep=';'),
        file_name = 'dataset_ifood',
        mime = 'text/csv'
)

#============================================================================
st.write('# EDA- Desafio Ifood')
st.markdown("""---""")


st.markdown(
    """
    O conjunto de Dados é composto por clientes da empresa Ifood com dados sobre:
    - Perfis de clientes;
    - Preferências do produto;
    - Scessos/Fracassos da campanha
    - Desempenho do canal
    
    ### Como utilizar este Dashboard?
    No menu lateral deste Web App há duas páginas:
    - **Conceitos de Estatística Descritiva:** Uma breveexplicação sobre conceitos estatísticas de Tendência Central;
    - **EDA Análise:** Uma breve análise exploratória dos Dados;
    
    
    Portanto, acesse o menu lateral e escolha a página que gostaria de visualizar!
    
    ### Time de Desenvolvimento:
    - Vinicius Borges
    
    ### Contact:
    - Vinicius Borges: https://www.linkedin.com/in/viniciusleitedata/
    - Blog Vorges: www.vorges.com.br
    
    ### Observação:
    - O desafio foi proposto pela professora Renata Biaggi
    - E.B.A - Estatística do Básico ao Avançado
    - https://www.renatabiaggi.com/
    """
)
st.markdown("""---""")