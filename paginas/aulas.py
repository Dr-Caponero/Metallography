import streamlit as st
import os
import pandas as pd 
import re
from openai import OpenAI 


st.markdown('✨**Conteúdo de Aula** - selecione a aula na barra lateral e use os recursos AI ao fim do conteúdo selecionado.')
st.divider()
def st_markdown(markdown_string):
    parts = re.split(r"!\[(.*?)\]\((.*?)\)", markdown_string)
    for i, part in enumerate(parts):
        if i % 3 == 0:
            st.markdown(part)
        elif i % 3 == 1:
            title = part
        else:
            st.image(part)  # Add caption if you want -> , caption=title)


# Função para buscar arquivos markdown no diretório de aulas
def buscar_aulas(diretorio):
    return [f for f in os.listdir(diretorio) if f.endswith('.txt')]

# Função para ler o conteúdo de uma aula em markdown
def ler_aula(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        return f.read()

# Diretório onde as aulas estão armazenadas
diretorio_aulas = 'Aulas' 

# Busca as aulas no diretório
aulas = buscar_aulas(diretorio_aulas)

def aux(x):
    return x[:-4]
# Widget de seleção de aula
aula_selecionada = st.sidebar.selectbox('Selecione uma aula:', sorted(aulas), index = 0, format_func = aux)
 
caminho_aula = os.path.join(diretorio_aulas, aula_selecionada)
conteudo_aula = ler_aula(caminho_aula)
st_markdown(conteudo_aula)


dificuldade_selecionada = st.sidebar.selectbox('Selecione a dificuldade dos exercícios:', {'Fácil', 'Média', 'Difícil', 'Muito Difícil'})


st.divider()
abas = ['Exercícios AI', 'Lista de Insights AI', 'Comentários']

aba1, aba2, aba3 = st.tabs(abas)

with aba1:
    st.header(abas[0]) 

    if st.button('✨ Gerar Lista de Exercícios dessa Lição', type = 'primary'): 

        # Configurações de API 
        openai_api_key = st.secrets["OPENAI_API_KEY"]
        client = OpenAI(api_key=openai_api_key)
        modelo = 'gpt-4o-mini'
         
        # Mensagem inicial do assistente no chat
        prompt = f"""
        Você é um assistente de professor da disciplina de Metalografia e Tratamentos Térmicos, para o curso técnico de metalurgia, cuja tarefa é escrever uma lista de exercicios baseado no <material de aula> abaixo. 
        Não se limite aos exemplos do <material de aula>, use outros exemplos que sejam pertinentes.
        Você deve fazer 3 exercícios abertos (discursivos) e 3 exercícios de teste (objetivos). Nos abertos, deve ser feita uma pergunta aberta. 
        Nos exercicios do tipo teste, deve ter uma pergunta e 4 alternativas de resposta, da qual apenas uma seja correta.
        Cada alternativa deve estar em uma linha. 
        Não diga qual resposta é a correta. 
        A dificuldade dos exercícios deve ser <dificuldade>. Não diga qual a dificuldade do exercício.
        O output deve conter os 3 exercicios abertos seguidos dos 3 exercicios de teste, seguido de uma breve resolução dos exercícios abertos e o gabarito dos exercicios de teste, separados por sessão. 
        No seu output, deve contar apenas o exercício, nada a mais, nada a menos. 
        Use formatação quando necessário, use negrito e italico para destacar o que for importante e emojis quando pertinente. 

        <material de aula>
        {conteudo_aula}
        </material de aula>

        <dificuldade>
        {dificuldade_selecionada}
        </dificuldade>    
         """ 

        # Faz uma requisição à API OpenAI para gerar a resposta do assistente
        with st.chat_message("assistant", avatar = '👨🏼‍🏫'):
            stream = client.chat.completions.create(
                model=modelo,
                messages= [{"role": "user", "content": prompt}],
                stream=True
            )

            # Exibe a resposta em tempo real
            response = st.write_stream(stream)


with aba2:
    st.header(abas[1]) 

    if st.button('✨ Gerar Lista de Insights dessa Aula', type = 'primary'): 

        # Configurações de API 
        openai_api_key = st.secrets["OPENAI_API_KEY"]
        client = OpenAI(api_key=openai_api_key)
        modelo = 'gpt-4.1-nano'
         
        # Mensagem inicial do assistente no chat
        prompt = f"""Você é um assistente de professor da disciplina de Metalografia e Tratamentos Térmicos, para o curso técnico de metalurgia, que tem a função de utilizar o <material de aula> e processar seguindo as seguintes instruções:
        - Leia e compreenda integralmente o material de aula para captar o contexto, os tópicos abordados e a progressão dos conceitos.
        - Escreva um output que seja uma coleção de 10 insights sobre a aula.
        - Use bullet points para cada insight. 
        - use texto normal nos titulos das sessões. 
        - cada insight deve ter no máximo 140 caracteres.
        - seu output deve ser apenas, e somente apenas, a lista de insights.
        - use negrito e italico para destacar o que for importante.
        - Não se limite aos exemplos do <material de aula>, use outros exemplos que sejam pertinentes.
                 
        O material da aula é o seguinte:
        <material de aula>
        {conteudo_aula}
        </material de aula>

        """

        # Faz uma requisição à API OpenAI para gerar a resposta do assistente
        with st.chat_message("assistant", avatar = '👨🏼‍🏫'):
            stream = client.chat.completions.create(
                model=modelo,
                messages= [{"role": "user", "content": prompt}],
                stream=True
            )

            # Exibe a resposta em tempo real
            response = st.write_stream(stream)
with aba3:
    st.header(abas[2])

    if st.button('✨ Comentários', type = 'primary'):

        # Configurações de API
        openai_api_key = st.secrets["OPENAI_API_KEY"]
        client = OpenAI(api_key=openai_api_key)
        modelo = 'gpt-4.1-nano'

    # Seção para Comentários
    st.subheader("Deixe seu Comentário sobre a Aula:")

    # Coleta do nome, comentário e nota do aluno
    nome = st.text_input("Seu nome:")
    comentario = st.text_area("Seu comentário:")
    nota = st.slider("Avalie a aula (1 a 5)", 1, 5)

    if st.button("Inserir Comentário"):
        if nome and comentario:
            # Aqui você pode salvar os dados em um arquivo CSV ou banco de dados
            novo_comentario = {"nome": nome, "comentario": comentario, "nota": nota}

            # Exemplo de salvar no arquivo CSV
            if os.path.exists("comentarios.csv"):
                comentarios = pd.read_csv("comentarios.csv")
                comentarios = comentarios.append(novo_comentario, ignore_index=True)
                comentarios.to_csv("comentarios.csv", index=False)
            else:
                pd.DataFrame([novo_comentario]).to_csv("comentarios.csv", index=False)

            st.success("Comentário postado com sucesso!")
        else:
            st.error("Por favor, preencha todos os campos.")

    # Exibir os comentários mais recentes
    if os.path.exists("comentarios.csv"):
        comentarios = pd.read_csv("comentarios.csv")
        comentarios_ordenados = comentarios.sort_values(by="nota", ascending=False)
        st.subheader("Comentários Recentes:")
        for index, row in comentarios_ordenados.iterrows():
            st.markdown(f"**{row['nome']}** - Nota: {row['nota']}")
            st.markdown(f"\"{row['comentario']}\"")
            st.markdown("---")
