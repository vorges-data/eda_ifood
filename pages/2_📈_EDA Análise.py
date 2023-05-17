import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly as plt
import plotly.express as px
from IPython.display import Image
from scipy.stats import skew
import plotly.figure_factory as ff

# Import Dataset
df = pd.read_csv('/home/vinicius/repos/eba_estatistica/estatistica_descritiva/dataset/mkt_data.csv')

#========================================================================
#========================== Funçoes Aux ================================
#========================================================================
null_columns = [
"marital_Divorced"
,"marital_Married"
,"marital_Single"
,"marital_Together"
,"marital_Widow"
,"education_2n Cycle"
,"education_Basic"
,"education_Graduation"
,"education_Master"
,"education_PhD"
]

for item in null_columns:
    df['bool_'+ str(item)] = np.where( df[item].isnull(), 0, 1)
#========================================================================
#========================== Menu Lateral ================================
#========================================================================
st.set_page_config(page_title='EDA', page_icon='📈', layout='wide')

st.header('Vorges Analysis: EDA')

st.sidebar.markdown('## Filtros')

#========================================================================
# Filtros
#========================================================================
kids = st.sidebar.multiselect(
    'Escolha o número de filhos:',
    df.loc[:,'kids'].unique().tolist(),
    default=[0,1,2,3]
)
st.sidebar.markdown("""---""")

education_level = st.sidebar.multiselect(
    'Escolha o grau de instrução:',
    df.loc[:,'education_level'].unique().tolist(),
    default=['Graduation', 'PhD', 'Master', 'Basic', '2n Cycle']
)
st.sidebar.markdown("""---""")

marital_status = st.sidebar.multiselect(
    'Escolha o Estado Civil:',
    df.loc[:,'marital_status'].unique().tolist(),
    default=['Single', 'Together', 'Married', 'Divorced', 'Widow']
)
st.sidebar.markdown("""---""")

st.markdown('### Perguntas de Negócio')
st.markdown("""---""")

#========================================================================
st.markdown('##### 1. Quantos Dados temos na base?')
qt_lines = df.shape[0]
qt_cols = df.shape[1]
st.write(f'Número de linhas: {qt_lines}')
st.write(f'Número de colunas: {qt_cols}')
st.markdown("""---""")
#========================================================================

st.markdown('##### 2. Quais são as colunas numéricas?')
st.markdown('''

Income, Kidhome, Teenhome, Recency, MntWines,
       MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts,
       MntGoldProds, NumDealsPurchases, NumWebPurchases,
       NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth,
       AcceptedCmp3, AcceptedCmp4, AcceptedCmp5, AcceptedCmp1,
       AcceptedCmp2, Complain, Z_CostContact, Z_Revenue, Response,
       Age, Customer_Days, marital_Divorced, marital_Married,
       marital_Single, marital_Together, marital_Widow,
       education_2n Cycle, education_Basic, education_Graduation,
       education_Master, education_PhD, MntTotal, MntRegularProds,
       AcceptedCmpOverall, kids, expenses

''')
st.markdown("""---""")
#========================================================================

st.markdown('##### 3. Há dados duplicados?')
st.write('Não há dados duplicados na base')
st.markdown("""---""")

#========================================================================

st.markdown('##### 4. Há dados nulos nessa base? Será que eles indicam algo? O que fazer com eles?')
st.write('Sim, há 10 colunas com dados vazio, estão demonstradas abaixo com a quantidade de dados nulos')
st.write('''
- marital_Divorced        1975
- marital_Married         1351
- marital_Single          1728
- marital_Together        1637
- marital_Widow           2129
- education_2n Cycle      2007
- education_Basic         2151
- education_Graduation    1092
- education_Master        1841
- education_PhD           1729

''')
st.markdown('''Os dados nulos podem carregar algum tipo de informação importante para o estudo, e por este motivo devemos analisa-los com calma, uma prática muito utilizada é a remoção desses dados por ser mais rápido e prático, mas nem sempre é a melhor estratégia, por exemplo, neste conjunto de dados se pergarmos a coluna 'education_master' só tem dados preenchidos com 4.0, que aparecem 364 vezes, o restante dos dados são nulos, isto é um forte indicativo que o dado nulo significa que a pessoa não tem aquela atribuição, neste caso seria a educação Mestrado.''')
st.markdown("""---""")

#========================================================================

st.markdown('##### 5. Qual é a média, mediana, 25 percentil, 75 percentil, mínimo e máximo das colunas income, kids e expenses?')
st.dataframe(df[['kids', 'Income','expenses']].describe())
st.markdown("""---""")

#========================================================================

st.markdown('##### 6. Qual é o maior salário encontrado na nossa base?')
st.write(df['Income'].max())
st.markdown("""---""")

#========================================================================

st.markdown('##### 7. Qual é a distribuição de salário na nossa base?')
# Histogram
fig = px.histogram(df['Income'])
st.plotly_chart(fig)

#Boxplot
fig = px.box(df['Income'])
st.plotly_chart(fig)
st.markdown("""---""")

#========================================================================

st.markdown('##### 8. Nossos clientes tem níveis de educação maiores ou menores?')
linhas_selecionadas = df['education_level'].isin(education_level)
df = df.loc[linhas_selecionadas, :]
fig = px.bar(df, x = df['education_level'], color='education_level')
st.plotly_chart(fig)
st.write('Grande parte de nossos clientes tem graduação completa')
st.markdown("""---""")

#========================================================================

st.markdown('##### 9. Quantos clientes temos em cada estado civil?')
linhas_selecionadas = df['marital_status'].isin(marital_status)
df = df.loc[linhas_selecionadas, :]
fig = px.bar(df, x = df['marital_status'], color='marital_status')
st.plotly_chart(fig)
st.write('Maior parte dos clientes são casados ou moram juntos (Together). Poucos são viúvos.')
st.markdown("""---""")

#========================================================================

st.markdown('##### 10. Qual é a relação de estado civil com número de filhos? Será que as pessoas casadas têm um maior número de filhos?')
linhas_selecionadas = df['kids'].isin(kids)
df = df.loc[linhas_selecionadas, :]
fig = px.box(df, x='marital_status', y='kids', color="marital_status")
st.plotly_chart(fig)

st.dataframe(df.groupby(['marital_status'])['kids'].describe())

st.write('Média de filhos por status de união')
st.dataframe(df.groupby('marital_status')['kids'].mean())

st.write('Mediana de filhos por status de união')
st.dataframe(df.groupby('marital_status')['kids'].median())
st.markdown("""---""")

#========================================================================

st.markdown('##### 11. As pessoas gasram mais ou menos em nossa plataforma quando têm filhos?')
fig = px.box(df, x='kids', y='expenses', color='kids')
st.plotly_chart(fig)

st.write('Média de gasto por quantidade de filhos')

st.dataframe(df[['kids','expenses']].groupby('kids').mean())

st.write('Mediana')
st.dataframe(df[['kids','expenses']].groupby('kids').median())

st.write('Podemos ver que tanto a média quanto a mediana 0 e 1 filho é maior nessa amostra de dados, porém a média de 2 filhos é menor do que de 3 filhos, enquanto a mediana de 2 filhos é maior do que de 3 filhos. Ambos os grupos 2 e 3 tem médias bem maiores do que a mediana, indicando outliers superiores (o próprio gráfico já mostra isso). Grupo 1 também tem outliers superiores, mas essa diferença é menos acentuada. Pessoas com nenhum filho tem uma distribuição um pouco mais similar a uma normal (sem outliers, e mediana levemente centrada do meio do boxplot)')

st.markdown("""---""")

#========================================================================

st.markdown('##### 12. Pessoas que têm um maior salário gastam mais?')
st.write('Para responder esta pergunta, vamos utilizar um gráfico de dispersão mostrando os gastos versus os ganhos.')
fig = px.scatter(df, x='expenses', y='Income')
st.plotly_chart(fig)

st.write('Vamos calcular a correlação de Pearson')
st.write(df['expenses'].corr(df['Income']))
st.markdown("""---""")

#========================================================================

st.markdown('##### 13. Pessoas com maior número de filhos gastam menos?')
fig = px.scatter(df, x='expenses', y='Income', color='kids')
st.plotly_chart(fig)
st.write('Sim, podemos perceber que pessoas com maior número de filhos acabam gastando menos.')
st.markdown("""---""")

#========================================================================

st.markdown('##### 14. Pessoas mais velhas gastam mais?')
fig = px.bar(df, x='Age', y='expenses', color='Age')
st.plotly_chart(fig)

st.write('Skew Expenses')
st.write(skew( df['expenses']))

#========================================================================

st.markdown('##### 15. Quais idades recebem mais?')
fig = px.bar(df, x='Age', y='Income', color='Age')
st.plotly_chart(fig)

st.write('Skew Income')
st.write(skew( df['Income']))