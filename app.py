import streamlit as st
import pandas as pd
from lists_daitai import personagens_daitai, get_rank, get_mod, MAPA_PERICIAS
import random

def renderizar_pericias(p):
    """Gera os dados da tabela de perícias"""
    dados_tabela = []
    pericias_investidas = p.get("Pericias_Investidas", {})
    atributos = p["Atributos"]

    for pericia, atr_base in MAPA_PERICIAS.items():
        mod_base = get_mod(atributos[atr_base])
        pp_investidos = pericias_investidas.get(pericia, 0)
        total = mod_base + pp_investidos
        
        destaque = f"{total} (+{pp_investidos} PP)" if pp_investidos > 0 else f"{total}"
        
        dados_tabela.append({
            "Perícia": pericia,
            "Atributo Base": atr_base,
            "Modificador Total": destaque
        })
    return pd.DataFrame(dados_tabela)

def renderizar_talentos(p):
    """Gera os dados da tabela de talentos"""
    talentos = p.get("Talentos", {})
    dados_tabela = [{"Talento": nome, "Descrição": desc} for nome, desc in talentos.items()]
    return pd.DataFrame(dados_tabela)

def mostrar_ficha_daitai():
    st.title("Academia Daitai Sunpo - Registro de Magos")
    
    char_sel = st.selectbox("Selecione o Personagem", list(personagens_daitai.keys()))
    p = personagens_daitai[char_sel]
    
    # Cabeçalho da Ficha
    col_foto, col_info = st.columns([1, 3])
    
    with col_foto:
        st.image(p["Foto"], use_container_width=True)
        
    with col_info:
        st.header(char_sel)
        st.subheader(f"*{p['Titulo']}*")
        st.subheader(f"*{p['Raça']}*")
        
        # Linha de Status (Nível e Rank)
        c1, c2, c3 = st.columns(3)
        c1.write(f"**Nível:** {p['Nivel']}")
        c2.write(f"**Rank:** {get_rank(p['Nivel'])}") # Rank Automático
        c3.write(f"**Classe:** {p['Especializacao']}")

        # Insígnias de Elementos
        st.write("**Afinidades Elementais:**")
        cols_elem = st.columns(len(p["Elementos"]))
        for i, elem in enumerate(p["Elementos"]):
            # Cores baseadas nos elementos do sistema
            cor = {"Piro": "red", "Hidro": "blue", "Geo": "orange", "Aero": "gray"}.get(elem, "green")
            cols_elem[i].markdown(f"**:{cor}[{elem}]**")

    st.divider()

    # Seção de Atributos
    st.markdown("### Atributos e Modificadores")
    at = p["Atributos"]
    
    # Grid de Atributos (Oficiais do Daitai Sunpo: FOR, INT, DES, RES, VON)
    col_at1, col_at2, col_at3, col_at4, col_at5 = st.columns(5)
    
    atributos_lista = [
        (col_at1, "FOR", at["FOR"]),
        (col_at2, "INT", at["INT"]),
        (col_at3, "DES", at["DES"]),
        (col_at4, "RES", at["RES"]),
        (col_at5, "VON", at["VON"])
    ]

    for col, nome, valor in atributos_lista:
        mod = get_mod(valor)
        sinal = "+" if mod >= 0 else ""
        col.metric(label=nome, value=valor, delta=f"{sinal}{mod}")

    # Valores Derivados Automáticos[cite: 3]
    st.markdown("---")
    res_mod = get_mod(at["RES"])
    von_mod = get_mod(at["VON"])
    
    pv_max = 50 + (5 * res_mod) + (15 * (p["Nivel"] - 1))
    pm_max = 100 + (10 * von_mod) + (20 * (p["Nivel"] - 1))
    pa_base = 10 + get_mod(at["DES"]) + von_mod
    
    d1, d2, d3 = st.columns(3)
    d1.metric("Pontos de Vida (PV)", pv_max)
    d2.metric("Pontos de Mana (PM)", pm_max)
    d3.metric("Defesa (PA)", pa_base)

    st.divider()

    # Colunas para organizar botões de utilitários
    col_btn1, col_btn2 , col_btn3 = st.columns([1, 2, 3])

    with col_btn1:
        # Botão estilo Popover (abre uma janelinha por cima)
        with st.popover("Ver Perícias"):
            st.markdown(f"### Perícias de {char_sel}")
            df_pericias = renderizar_pericias(p)
            
            # Exibe a tabela sem o índice lateral para ficar mais limpo
            st.table(df_pericias)
            
            st.caption("Ponto de Perícia (PP) investido conforme o Nível.")

    with col_btn2:
        # Exemplo de outro botão utilitário que você pode querer futuramente
        if st.button("Rolar Iniciativa"):
            iniciativa = random.randint(1, 20) + get_mod(p["Atributos"]["DES"])
            st.info(f"Resultado da Iniciativa: **{iniciativa}**")

    with col_btn3:
        # Exemplo de outro botão utilitário que você pode querer futuramente
        if st.button("Ver Talentos"):
            st.info(f"Talentos de {char_sel}:")
            df_talentos = renderizar_talentos(p)
            st.table(df_talentos)

mostrar_ficha_daitai()