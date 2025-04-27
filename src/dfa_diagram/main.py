import streamlit as st
from graphviz import Digraph
import pandas as pd

st.title("Gerador de Diagramas de Autômatos")

st.subheader("Defina os Estados e os Símbolos de Entrada")

entrada_estados = st.text_input(
    "Estados (separados por vírgula):", value="A,B,C")
estados = [estado.strip()
           for estado in entrada_estados.split(',') if estado.strip() != ""]

entrada_simbolos = st.text_input(
    "Símbolos de Entrada (separados por vírgula):", value="0,1")
simbolos = [simbolo.strip()
            for simbolo in entrada_simbolos.split(',') if simbolo.strip() != ""]

if estados and simbolos:
    st.subheader("Edite a Tabela de Transições")

    tabela_transicoes = pd.DataFrame(index=estados, columns=simbolos)
    for estado in estados:
        for simbolo in simbolos:
            tabela_transicoes.loc[estado, simbolo] = ''

    tabela_editada = st.data_editor(tabela_transicoes, num_rows="dynamic")

    st.subheader("Defina o Estado Inicial e os Estados de Aceitação")
    estado_inicial = st.selectbox("Estado Inicial:", estados)
    estados_finais = st.multiselect("Estados de Aceitação:", estados)

    if st.button("Gerar Diagrama"):
        grafo = Digraph(comment='Autômato Personalizado')

        for estado in estados:
            if estado in estados_finais:
                grafo.node(estado, shape='doublecircle')
            else:
                grafo.node(estado)

        grafo.node('', shape='none')
        grafo.edge('', estado_inicial)

        for estado_origem in estados:
            for simbolo in simbolos:
                estado_destino = tabela_editada.loc[estado_origem, simbolo]
                if estado_destino and estado_destino.strip() != '':
                    destinos = [e.strip() for e in estado_destino.split(',')]
                    for destino in destinos:
                        grafo.edge(estado_origem, destino, label=simbolo)

        st.subheader("🎯 Diagrama Gerado:")
        st.graphviz_chart(grafo)
        grafo.render('diagrama_automato', format='png', cleanup=True)
        st.success("✅ Arquivo 'diagrama_automato.png' gerado com sucesso!")
else:
    st.warning(
        "🚨 Por favor, informe pelo menos um estado e um símbolo de entrada para continuar.")
