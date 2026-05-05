import streamlit as st
from lists_daitai import personagens_daitai, get_rank, get_mod

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

mostrar_ficha_daitai()