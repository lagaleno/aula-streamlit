import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Organizando Dataset
df = pd.read_csv('performance-alunos/StudentsPerformance.csv')
df = df.drop(["gender", "race/ethnicity", "lunch"], axis=1)

# Gerando visualizações
df_grouped = df.groupby('parental level of education').size() # quantidade de valores de cada valor da coluna "parental level of education"

# Assumindo que df_grouped é o resultado da operação de groupby
# Agrupa os dados pela coluna 'parental level of education' e conta as ocorrências
df_grouped = df.groupby('parental level of education').size()

# Criando o gráfico de barras horizontal
fig_barh = plt.figure(figsize=(10, 6))  # Ajusta o tamanho da figura
df_grouped.plot(kind='barh', color='skyblue')  # 'barh' cria barras horizontais

# Adiciona o título e os rótulos dos eixos
plt.title('Contagem do Nível de Educação dos Pais')  # Título do gráfico
plt.xlabel('Contagem')  # Rótulo do eixo X (quantidade)
plt.ylabel('Nível de Educação dos Pais')  # Rótulo do eixo Y (categorias)


# Criando o histograma
scores = df['math score']  # Substitua pelo nome real da coluna de pontuação
fig_hist = plt.figure(figsize=(10, 6))  # Ajusta o tamanho da figura
plt.hist(scores, bins=10, color='skyblue', edgecolor='black')  # 'bins' ajusta o número de intervalos

# Adiciona o título e os rótulos dos eixos
plt.title('Distribuição das Pontuações dos Alunos')  # Título do gráfico
plt.xlabel('Pontuação')  # Rótulo do eixo X (valores de pontuação)
plt.ylabel('Frequência')  # Rótulo do eixo Y (frequência de cada intervalo)

# Construindo visualização no Streamlit
st.write("# Performance de Estudantes") # escreve um texto na interface (a # coloca a formatação de título)

st.write("## Dataset Utilizado") # (os dois ## são úteis para colocar subtítulo)
st.dataframe(df)
st.write("Fonte do Dataset: [Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)") # dessa forma é posto um texto normal

# Exibe o gráfico no Streamlit
st.write("## Visualizações dos dados")

st.write("### Barra Horizontal") # (com ### seria "subsubtítulo")
st.pyplot(fig_barh) # o pyplot serve para exibir o gráfico construído com matplotlib

st.write("### Histograma")
st.pyplot(fig_hist)

