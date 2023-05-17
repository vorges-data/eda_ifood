import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import plotly as plt
import plotly.express as px
from IPython.display import Image
from scipy.stats import skew
import plotly.figure_factory as ff
import streamlit as st
from PIL import Image


# Título
st.markdown('# Estatística Descritiva')

# Texto
st.markdown("""
    
    Olá neste artigo iremos abordar alguns conceitos importantes da Estatística de Primeira Ordem, conceitos estes fundamentais na etapa de exploração dos dados e geração de insghts para responder algumas perguntas essenciais para o negócio! Ao lado, você pode conferir a Exploração dos Dados utilizando alguns dos conceitos que veremos abaixo. Vamos nessa?
    
    ##### O que são as medidas de Tendência Central?
    
    As medidas de tendência central são estatísticas descritivas que representam um valor central ou típico em um conjunto de dados. Elas são utilizadas para resumir e descrever as características dos dados, fornecendo uma medida que representa a localização central dos valores.

    As três medidas de tendência central mais comumente utilizadas são a média, a mediana e a moda:
    
    
    **Média:** é a medida de tendência central mais conhecida e é calculada somando todos os valores do conjunto de dados e dividindo pelo número total de valores. A média é sensível a valores extremos, pois eles podem afetar seu valor de forma significativa.
    
    
    Dados os $n$ números ${\{x_{1}, x_{2}, \ldots, x_{n}\}}$, a média aritmética é definida como:
""")


st.latex(r'''
    
    \bar {x} = {\frac{1}{n}} \sum_{i = 1}^{n}x_{i} ={\frac{x_{1} + x_{2} + \cdots + x_{n}}{n}}

''')

st.markdown("""---""")

st.markdown("""
    
    **Mediana:** é o valor que divide o conjunto de dados em duas partes iguais, ou seja, metade dos valores está abaixo da mediana e metade está acima. Para calcular a mediana, os valores são ordenados em ordem crescente e o valor central é selecionado. A mediana é menos sensível a valores extremos, tornando-a uma medida mais robusta em relação à média.
    
    

""")

st.markdown("""
    
   Sejam: ${x_{1}, x_{2}, x_{3}, \ldots, x_{n}}$ os dados de uma amostra ordenada em ordem crescente e designando a mediana como $M_{e}$, distinguimos dois casos:
   
   
   Sejam ${x_{1}, x_{2}, x_{3}, \ldots, x_{n}}$ os dados de uma amostra ordenada em ordem crescente e designando a mediana como $M_{e}$, distinguimos dois casos:

    **a)** Se $n$ for ímpar, a mediana é o valor que ocupa a posição:


""")

st.latex(r'''
    
   \frac{(n + 1)}{2}

''')

st.markdown("""

Uma vez ordenados os dados, em ordem crescente ou decrescente, pois este é o valor central. Ou seja: $M_{e}=x_{{(n+1)/2}}$.

""")

st.markdown("""

 b) Se $n$ for par, a mediana é a média aritmética dos dois valores centrais. Quando $n$ é par, os dois dados no centro da amostra ocupam as posições:

 
""")

st.latex(r'''
    
    \frac{n}{2}
    
''')

st.write('e também a posição:')

st.latex(r'''
    
     \frac{n}{2} + 1
    
''')

st.markdown("""---""")

st.markdown("""
    
   
    **Moda:** é o valor mais frequente no conjunto de dados. Em outras palavras, é o valor que ocorre com maior frequência. Um conjunto de dados pode ter uma moda única (unimodal) quando há um valor com maior frequência, ou pode ter várias modas (multimodal) quando existem dois ou mais valores com frequências semelhantes.

""")

st.markdown("""---""")

st.write('Essas medidas de tendência central são úteis para resumir conjuntos de dados e fornecer uma ideia geral da localização central dos valores.')

st.markdown("""
    
    ### Quartis e Boxplot
    

Os quartis dividem um conjunto de dados ordenado em quatro partes iguais, representando assim os pontos de divisão da distribuição em quartis: 

- **O primeiro quartil (Q1):** é o valor abaixo do qual 25% dos dados estão localizados; 
- **O segundo quartil (Q2):** é a mediana, ou seja, o valor abaixo do qual 50% dos dados estão localizados; 
- **O terceiro quartil (Q3):** é o valor abaixo do qual 75% dos dados estão localizados.

**Amplitude interquartílica:**	A distância entre o 1o. e o 3o. quartis (Q3-Q1); assim, ele ultrapassa o meio de 50% dos dados.
    
""")

image = Image.open('quartis.png')
st.image( image, caption= 'Quartis')

st.markdown("""

    **Boxplot**
Os boxplots (também conhecidos como diagramas de caixa) são gráficos que mostram a representação visual dos quartis e outros valores estatísticos importantes de um conjunto de dados. Eles são compostos por uma caixa retangular que representa o intervalo entre o primeiro quartil (Q1) e o terceiro quartil (Q3), com uma linha no meio que representa a mediana (Q2). Além disso, os boxplots podem incluir linhas chamadas de "whiskers" que se estendem a partir da caixa para mostrar a dispersão dos dados. Pontos fora das "whiskers" são considerados valores atípicos ou extremos.

Os boxplots fornecem uma representação gráfica rápida e eficaz da distribuição dos dados, permitindo identificar valores atípicos, a simetria da distribuição e a presença de assimetrias ou desvios. Eles são especialmente úteis quando se trabalha com conjuntos de dados grandes ou quando se deseja comparar várias distribuições lado a lado.

""")

image = Image.open('Boxplot.png')
st.image( image, caption= 'Boxplot')

st.markdown("""---""")

st.markdown("""
    
    ### Variáveis Numéricas e Categóricas
    
**Variáveis numéricas** são aquelas que representam quantidades (quantitativas) ou medidas e podem ser expressas em termos de números. Elas podem ser contínuas ou discretas.

- **Variáveis numéricas contínuas:** São aquelas que podem assumir qualquer valor dentro de um intervalo. Por exemplo, a altura de uma pessoa ou a temperatura de um dia podem ser variáveis contínuas, pois podem assumir qualquer valor dentro de um intervalo específico.

- **Variáveis numéricas discretas:** São aquelas que assumem apenas valores inteiros ou valores específicos em um conjunto finito. Por exemplo, o número de irmãos de uma pessoa ou o número de carros em um estacionamento são variáveis discretas.

**Variáveis categóricas**, também conhecidas como variáveis qualitativas, representam características ou atributos que não podem ser medidas numericamente. Elas são divididas em categorias ou classes distintas.

- **Variáveis categóricas nominais:** São aquelas em que as categorias não possuem uma ordem específica. Por exemplo, a cor dos olhos (azul, verde, castanho) ou o estado civil (solteiro, casado, divorciado) são variáveis categóricas nominais.

- **Variáveis categóricas ordinais:** São aquelas em que as categorias possuem uma ordem específica. Por exemplo, a classificação de nível educacional (ensino fundamental, ensino médio, graduação, pós-graduação) ou a escala de dor (sem dor, dor leve, dor moderada, dor intensa) são variáveis categóricas ordinais.

    
""")

image = Image.open('classificacao_variaveis.png')
st.image( image, caption= 'Classificação das Variáveis')

st.markdown("""---""")

st.markdown("""
    
    ###  Dispersão
A medida de dispersão permite entender a amplitude ou extensão dos valores dos dados, o grau de variabilidade entre eles e se os dados estão concentrados ou espalhados. Aqui estão algumas maneiras pelas quais a medida de dispersão contribui para o entendimento dos dados:

**Amplitude:** A medida de dispersão mais simples é a amplitude, que é a diferença entre o maior e o menor valor dos dados. Ela fornece uma ideia geral da variação total dos dados. 

    
""")

st.latex(r'''

    {\text{Amplitude} = \text{valor máximo} - \text{valor mínimo}}

''')

st.markdown("""

**Desvio médio absoluto:** Essa medida calcula a média das diferenças absolutas entre cada valor dos dados e a média. Quanto maior o desvio médio absoluto, maior é a dispersão dos dados.

    
""")

st.latex(r'''

   {\text{Desvio médio absoluto} = \frac{1}{n} \sum_{i=1}^{n} |x_i - \text{média}|
}


''')

st.markdown("""

**Variância:** A variância é a média dos quadrados das diferenças entre cada valor dos dados e a média. Ela mede o quão dispersos os dados estão em relação à média. Uma variância maior indica maior dispersão dos dados.

    
""")

st.latex(r'''

   {\text{Variância} = \frac{1}{n} \sum_{i=1}^{n} (x_i - \text{média})^2
}


''')

st.markdown("""

**Desvio padrão:** O desvio padrão é a raiz quadrada da variância e é uma das medidas de dispersão mais comumente usadas. Ele indica o quanto os dados se desviam da média. Um desvio padrão maior indica maior dispersão dos dados.

    
""")

st.latex(r'''

  {\text{Desvio padrão} = \sqrt{\text{Variância}}
}

''')

st.markdown("""

**Intervalo interquartil:** Esse é o intervalo entre o primeiro quartil (25%) e o terceiro quartil (75%) dos dados. Ele é útil para detectar a presença de valores extremos e proporciona uma medida robusta de dispersão, menos influenciada por valores discrepantes.

    
""")

st.markdown("""---""")

st.markdown("""
    
    ###  Skew

**Skewness (ou assimetria)** é uma medida estatística que descreve a assimetria da distribuição de uma variável. Em outras palavras, ela quantifica o grau de distorção ou inclinação da distribuição em relação à sua média.

Uma distribuição simétrica tem skewness igual a zero, o que significa que a curva é simétrica em relação à sua média. Uma distribuição com skewness positiva tem uma cauda alongada à direita da distribuição, indicando uma assimetria positiva. Por outro lado, uma distribuição com skewness negativa tem uma cauda alongada à esquerda da distribuição, indicando uma assimetria negativa.

A interpretação da skewness é a seguinte:

- Se a skewness é maior que zero, a distribuição é assimétrica positiva.
- Se a skewness é menor que zero, a distribuição é assimétrica negativa.
- Se a skewness é igual a zero, a distribuição é simétrica.
""")

image = Image.open('skew.png')
st.image( image, caption= 'Skewness')

st.markdown("""
    #####  Fórmula da Skew:
""")

st.latex(r'''

{\text{Skewness} = \frac{\frac{1}{n} \sum_{i=1}^{n} (x_i - \text{média})^3}{\left(\frac{1}{n} \sum_{i=1}^{n} (x_i - \text{média})^2\right)^{\frac{3}{2}}}
}

''')

st.write('A skewness é uma medida importante, pois fornece informações sobre a forma da distribuição dos dados. Ela pode ajudar a identificar se os dados possuem uma inclinação em direção a valores mais altos ou mais baixos e a determinar se existem valores extremos ou outliers que afetam a distribuição.')