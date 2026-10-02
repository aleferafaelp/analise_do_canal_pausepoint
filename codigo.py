# Título: Análise de Conteúdo - PausePoint

# Seção: Adicionar vídeos
    # Número do vídeo
    # Data de publicação
    # Tipo do vídeo
    # Tipo do vídeo (inglês)
    # Visualizações
    # Dia da Semana
    # Horário de publicação
    # Botão: Adicionar vídeo
        # Quando o botão "Adicionar vídeo" é clicado, o vídeo é adicionado à tabela de vídeos adicionados.

# Seção: Vídeos adicionados
    # Tabela de vídeos adicionados
    # Editar e excluir vídeos adicionados

# Seção: Dashboard
    # Visualizações totais
    # Gráfico de barras - visualizações por (filtro)
    # Gráfico de pizza - visualizações por tipo de vídeo

# Ferramentas: 
    # streamlit
    # pandas
    # ploty

import streamlit as st
import pandas as pd
import plotly.express as px

tabela_videos = pd.read_csv(
    "tabela_videos_corrigida.csv",
    sep=";",
    encoding="utf-8"
)

st.write("# Análise de Conteúdo - PausePoint")


st.sidebar.write("## Adicionar vídeos")

numero_video = st.sidebar.number_input("Número do vídeo", min_value=1, step=1)
data_publicacao = st.sidebar.date_input("Data de publicação")
tipo_video = st.sidebar.text_input("Tipo do vídeo")
tipo_video_ingles = st.sidebar.text_input("Tipo do vídeo (inglês)")
visualizacoes = st.sidebar.number_input("Visualizações", min_value=0, step=1)
dia_semana = st.sidebar.selectbox("Dia da Semana", options=["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"])
horario_publicacao = st.sidebar.time_input("Horário de publicação")
botao_adicionar = st.sidebar.button("Adicionar vídeo")

if botao_adicionar:
    nova_linha = pd.DataFrame({
        "Número do vídeo": [numero_video],
        "Data de publicação": [data_publicacao],
        "Tipo do vídeo": [tipo_video],
        "Tipo do vídeo (inglês)": [tipo_video_ingles],
        "Visualizações": [visualizacoes],
        "Dia da Semana": [dia_semana],
        "Horário de publicação": [horario_publicacao]
    })

    tabela_videos = pd.concat([tabela_videos, nova_linha], ignore_index=True)
    tabela_videos.to_csv("tabela_videos_corrigida.csv", sep=";", index=False, encoding="utf-8")
    st.success("Vídeo adicionado com sucesso!")



st.write("## Vídeos adicionados")

st.dataframe(tabela_videos)


st.write("## Dashboard")

visualizacoes = tabela_videos["Visualizações"].sum()
st.metric("Visualizações totais", visualizacoes)

grafico1 = px.bar(tabela_videos, x="Dia da Semana", y="Visualizações", color="Dia da Semana", color_discrete_map={
    "Segunda-feira": "#008080",
    "Terça-feira": "#008B8B",
    "Quarta-feira": "#20B2AA",
    "Quinta-feira": "#5F9EA0",
    "Sexta-feira": "#00CED1",
    "Sábado": "#48D1CC",
    "Domingo": "#66CDAA"
})

st.plotly_chart(grafico1)

grafico2 = px.pie(tabela_videos, values="Visualizações", names="Dia da Semana", hole=0.5, color_discrete_map={
    "Segunda-feira": "#008080",
    "Terça-feira": "#008B8B",
    "Quarta-feira": "#20B2AA",
    "Quinta-feira": "#5F9EA0",
    "Sexta-feira": "#00CED1",
    "Sábado": "#48D1CC",
    "Domingo": "#66CDAA"
})

st.plotly_chart(grafico2)