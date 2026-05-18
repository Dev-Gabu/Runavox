import streamlit as st
import pandas as pd
from lists_daitai import *
from personagens import personagens_daitai
import random

## FICHA BASE
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

## ITENS
def mostrar_inventario(p):
    st.markdown("### Inventário")
    
    inventario = p.get("Inventario", [])
    
    if not inventario:
        st.info("O inventário está vazio.")
        return

    for item in inventario:
        # Lógica do ícone conforme o tipo
        icon_path = ICON_MAP.get(item["Tipo"], "assets/material.png")
        
        # Criar a linha do item usando colunas para alinhar ícone e botão
        col_icon, col_btn = st.columns([1, 10])
        
        with col_icon:
            try:
                st.image(icon_path, width=30)
            except:
                st.write("📦") # Fallback caso a imagem não exista

        with col_btn:
            # Popover atua como a janela de detalhes ao clicar
            with st.popover(f"{item['Nome']} (x{item['Quantidade']})", use_container_width=True):
                st.markdown(f"**Nome:** {item['Nome']}")
                st.markdown(f"**Tipo:** {item['Tipo']}")
                st.markdown(f"**Quantidade:** {item['Quantidade']}")
                st.divider()
                st.markdown(f"**Descrição:**\n{item['Descrição']}")
                
                # Botão de uso rápido (Opcional)
                if item["Tipo"] == "Consumivel":
                    if st.button(f"Usar {item['Nome']}", key=f"use_{item['Nome']}"):
                        st.toast(f"Você usou {item['Nome']}!")

def mostrar_equipamento(p):
    st.markdown("### Equipamento")
    
    equipamento = p.get("Equipamento", [])
    
    if not equipamento:
        st.info("O equipamento está vazio.")
        return

    for item in equipamento:
        # Lógica do ícone conforme o tipo
        icon_path = ICON_MAP.get(item["Tipo"], "assets/material.png")
        
        # Criar a linha do item usando colunas para alinhar ícone e botão
        col_icon, col_btn = st.columns([1, 10])
        
        with col_icon:
            try:
                st.image(icon_path, width=30)
            except:
                st.write("📦") # Fallback caso a imagem não exista

        with col_btn:
            # Popover atua como a janela de detalhes ao clicar
            if item['Nome']:
                with st.popover(f"{item['Nome']}", use_container_width=True):
                    st.markdown(f"**Nome:** {item['Nome']}")
                    st.markdown(f"**Tipo:** {item['Tipo']}")
                    st.divider()
                    st.markdown(f"**Descrição:**\n{item['Descrição']}")
                    
                    if item["Tipo"] == "Consumivel":
                        if st.button(f"Usar {item['Nome']}", key=f"use_{item['Nome']}"):
                            st.toast(f"Você usou {item['Nome']}!")
            else:
                st.markdown(f"**Slot Vazio** - {item['Tipo']}")

## GRIMÓRIO
def mostrar_grimorio_conjurador(p):
    
    aba1, aba2 = st.tabs(["Ver Grimório", "Criar Novo Feitiço"])
    
    with aba1:
        st.subheader(f"Feitiços Conhecidos")
        grimorio = p.get("Grimorio", [])
        
        if not grimorio:
            st.info("Este mago ainda não transcreveu feitiços.")
        else:
            for spell in grimorio:
                with st.expander(f"✨ {spell['Nome']} (Comp: {spell['Complexidade']} | PM: {spell['Mana']})"):
                    st.write(f"**Tipo:** {spell['Tipo']}")
                    st.write(f"**Custo:** {spell['Mana']} PM")
                    st.write(f"**Elemento:** {spell['Elemento']}")
                    st.write(f"---")
                    st.write(spell['Descrição'])
                    if spell['Dano']  is not None: st.write(f"**Dano:** {spell['Dano'][0]}d{spell['Dano'][1]}")
                    if spell['Alcance'] is not None: st.write(f"**Alcance:** {spell['Alcance'] }")
                    if spell['Duração'] is not None: st.write(f"**Duração:** {spell['Duração'] }")

    with aba2:
        st.subheader("Criar Feitiço")
        
        # Cálculo do LC do personagem
        mod_int = get_mod(p["Atributos"]["INT"])
        lc_max = p["Nivel"] + mod_int
        st.info(f"Seu Limite de Complexidade (LC) Atual: **{lc_max}**")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            feitico = {
                "nome": "",
                "tipo": "",
                "descricao": "",
                "complexidade": 0,
                "mana": 0,
                "Elemento": "",
                "Dano": None,
                "Alcance": None,
                "Duração": None
            }

            feitico["nome"] = st.text_input("Nome do Feitiço", placeholder="Ex: Sopro de Inverno")
            
            # Seleção do Elemento
            feitico["Elemento"] = st.selectbox("Selecione o Elemento", TABELA_ELEMENTOS)

            # Seleção do Tipo Base
            lista_nomes_tipos = [t["Tipo"] for t in TABELA_A_TIPO_FEITICO]
            feitico["tipo"] = st.selectbox("Selecione o Tipo Base", lista_nomes_tipos)
            
            # Busca os dados do tipo selecionado
            dados_tipo = next(t for t in TABELA_A_TIPO_FEITICO if t["Tipo"] == feitico["tipo"])
            
            feitico["descricao"] = dados_tipo["Descrição"]
            feitico["Dano"] = dados_tipo["Dano"]
            feitico["Alcance"] = dados_tipo["Alcance"]

            if feitico["tipo"] == "Construção":
                res_mod = (p["Atributos"]["RES"] - 6) // 2
                feitico["Duração"] = f"{res_mod} turnos" if res_mod > 1 else "1 turno"
            else: feitico["Duração"] = dados_tipo["Duração"]

            st.caption(f"**Descrição Base:** {dados_tipo['Descrição']}")
            st.caption(f"**Alcance:** {dados_tipo['Alcance'] if dados_tipo['Alcance'] else 'Não especificado'} | **Duração:** {dados_tipo['Duração'] if dados_tipo['Duração'] else 'Não especificada'} | **Dano:** {dados_tipo['Dano'] if dados_tipo['Dano'] else 'Não especificado'}**")

            # Seleção de Modificadores
            lista_nomes_mods = [m["Modificador"] for m in TABELA_B_MOD_FEITICO]
            mods_selecionados_nomes = st.multiselect("Adicionar Modificadores", lista_nomes_mods)
            
        # Lógica de Cálculo
        comp_base = dados_tipo["Complexidade"]

        # Modificação do feitiço

        for mod in mods_selecionados_nomes:
            descricao_mod = ""

            if mod == "Alcance Aumentado":
                if feitico["Alcance"] is None:
                    feitico["Alcance"] = dados_tipo["Alcance"]
                if feitico["Alcance"] == "Pessoal":
                    feitico["Alcance"] = "Curto"
                elif feitico["Alcance"] == "Curto":
                    feitico["Alcance"] = "Médio"
                elif feitico["Alcance"] == "Médio":
                    feitico["Alcance"] = "Longo"
            elif mod == "Duração Aumentada":
                if feitico["Duração"] is None:
                    feitico["Duração"] = dados_tipo["Duração"]
                if feitico["Duração"] == "Instantâneo":
                    feitico["Duração"] = "1 Turno"
                elif feitico["Duração"] == "1 Turno":
                    feitico["Duração"] = "2 Turnos"
                elif feitico["Duração"] == "2 Turnos":
                    feitico["Duração"] = "3 Turnos"
                elif feitico["Duração"] == "3 Turnos":
                    feitico["Duração"] = "4 Turnos"
                elif feitico["Duração"] == "4 Turnos":
                    feitico["Duração"] = "5 Turnos"
                elif feitico["Duração"] == "5 Turnos":
                    feitico["Duração"] = "6 Turnos"
                elif feitico["Duração"] == "6 Turnos":
                    feitico["Duração"] = "7 Turnos"
                elif feitico["Duração"] == "7 Turnos":
                    feitico["Duração"] = "8 Turnos"
                elif feitico["Duração"] == "8 Turnos":
                    feitico["Duração"] = "9 Turnos"
                elif feitico["Duração"] == "9 Turnos":
                    feitico["Duração"] = "10 Turnos"
                elif feitico["Duração"] == "10 Turnos":
                    feitico["Duração"] = "Até o fim do combate"
            elif mod == "Área de Efeito (AoE)":
                descricao_mod += "Ataque em área de afeito de curto alcance. "
            elif mod == "Confiabilidade":
                descricao_mod += "CD para resistir ao efeito do feitiço aumenta em +2. "
            elif mod == "Potência Melhorada":
                if dados_tipo["Dano"] is not None:
                    feitico["Dano"] = (feitico["Dano"][0] + 1, feitico["Dano"][1])
            elif mod == "Dano Aumentado":
                if dados_tipo["Dano"] is not None:
                    if feitico["Dano"][1] < 12:
                        feitico["Dano"] = (feitico["Dano"][0], feitico["Dano"][1] + 2)
                    elif feitico["Dano"][1] == 12:
                        feitico["Dano"] = (feitico["Dano"][0], feitico["Dano"][1] + 8)
                    else: feitico["Dano"] = (feitico["Dano"][0], feitico["Dano"][1] + 2)
            elif mod == "Multi-alvo":
                descricao_mod += "Pode atingir múltiplos alvos. "
            elif mod == "Feitiço Sustentado":
                if feitico["Duração"] is not None and feitico["Duração"] != "Instantâneo":
                    descricao_mod += "O mago deve gastar sua Ação Completa para manter o feitiço ativo. "
            elif mod == "Requer Preparo":
                descricao_mod += "Requer um turno de preparação antes de ser lançado. "
            elif mod == "Efeito Secundário":
                descricao_mod += "Esse feitiço possui um efeito secundário. "

            if descricao_mod:
                if feitico["descricao"]:
                    feitico["descricao"] += " " + descricao_mod

        # Soma os custos dos modificadores selecionados
        custo_mods = 0
        for m_nome in mods_selecionados_nomes:
            m_dados = next(m for m in TABELA_B_MOD_FEITICO if m["Modificador"] == m_nome)
            custo_mods += m_dados["Custo"]
            
        complexidade_final = max(1, comp_base + custo_mods) # Complexidade mínima é 1
        custo_mana = complexidade_final * 5
        
        with col2:
            st.metric("Complexidade Total", f"{complexidade_final} / {lc_max}")
            st.metric("Custo de Mana", f"{custo_mana} PM")
            
            if complexidade_final > lc_max:
                st.error("⚠️ Complexidade excede seu limite!")
            else:
                st.success("✅ Feitiço viável!")

        # Resumo Técnico para o Jogador
        with st.expander("🔮 Visualizar Feitiço"):
            resumo = f"""
            **Feitiço:** {feitico["nome"] if feitico["nome"] else 'Sem Nome'} **[** {feitico["Elemento"]} **]** \n
            **Descrição:** {feitico["descricao"] if feitico["descricao"] else 'Sem descrição'}\n
            **Custo Final:** {custo_mana} de Mana\n
            **Modificadores:** {', '.join(mods_selecionados_nomes) if mods_selecionados_nomes else 'Nenhum'}\n
            **Alcance:** {feitico["Alcance"] if feitico["Alcance"] else 'Não especificado'}\n
            **Duração:** {feitico["Duração"] if feitico["Duração"] else 'Não especificada'}\n
            **Dano:** {f"**Dano:** {feitico['Dano'][0]}d{feitico['Dano'][1]}" if feitico["Dano"] else 'Não especificado'}\n
            """
            
            st.write(resumo)

        # Resumo Técnico para o Jogador
        with st.expander("📝 Detalhes Técnicos do Feitiço"):
            resumo = f"""
            {{\n
                "Nome": "{feitico['nome'] if feitico['nome'] else 'Sem Nome'}",\n
                "Tipo": "{feitico['tipo']}",\n
                "Elemento": "{feitico['Elemento']}",\n
                "Descrição": "{feitico['descricao'] if feitico['descricao'] else 'Sem descrição'}",\n
                'Complexidade': {complexidade_final},\n
                'Mana': {custo_mana},\n
                "Dano": {f"({feitico['Dano'][0]}, {feitico['Dano'][1]})" if feitico["Dano"] else "None"},\n
                "Alcance": "{feitico["Alcance"] if feitico["Alcance"] else None}",\n
                "Duração": "{feitico["Duração"] if feitico["Duração"] else None}",\n
                }},
            """
            
            st.write(resumo)

def mostrar_grimorio_invocador(p):
    
    aba1, aba2, aba3= st.tabs(["Invocações", "Criar Habilidade", "Criar Invocação"])
    
    with aba1:
        grimorio = p.get("Grimorio", [])
        
        if not grimorio:
            st.info("Este mago ainda não transcreveu feitiços.")
        else:
            for invocacao in grimorio:
                with st.expander(f"🦉 {invocacao['Nome']} | PV: {invocacao['PV']} | PA: {invocacao['PA']})"):
                    st.image(invocacao['Aparencia'], width=100)
                    st.write(f"**Descricao:** {invocacao['Descricao']}")
                    st.write(f"**Categoria:** {invocacao['Categoria']}")
                    st.write(f"**Elemento:** {invocacao['Elemento']}")
                    st.write(f"**Dano:** {invocacao['Dano fixo']} + {invocacao['Dano dado'][0]}d{invocacao['Dano dado'][1]}")
                    st.write(f"---")
                    st.write(invocacao['Descrição'])
                    
                    st.write("Atributos e Modificadores")
                    at = invocacao["Atributos"]
                    
                    col_at1, col_at2, col_at3, col_at4, col_at5, col_btn1 = st.columns(6)
                    
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

                    for habilidade in invocacao.get("Habilidades", []):
                        # Lógica para exibir habilidades da invocação
                        pass

    with aba2:
        st.subheader("Criar Habilidade")
    
    with aba3:
        st.subheader("Criar Invocação")
        

def mostrar_grimorio_mago_marcial(p):
    
        st.info("A seção de Grimório para Magos Marciais ainda está em desenvolvimento. Fique atento para futuras atualizações!")

## PÁGINA PRINCIPAL
def mostrar_ficha_daitai():
    st.title("Academia Daitai Sunpo - Registro de Magos")
    
    char_sel = st.selectbox("Selecione o Personagem", list(personagens_daitai.keys()))
    p = personagens_daitai[char_sel]
    
    st.divider()

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
    col_at1, col_at2, col_at3, col_at4, col_at5, col_btn1 = st.columns(6)

    with col_btn1:
        # Botão estilo Popover (abre uma janelinha por cima)
        with st.popover("Ver Perícias"):
            st.markdown(f"### Perícias de {char_sel}")
            df_pericias = renderizar_pericias(p)
            
            # Exibe a tabela sem o índice lateral para ficar mais limpo
            st.table(df_pericias)
            
            st.caption("Ponto de Perícia (PP) investido conforme o Nível.")
    
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
    st.markdown("### Atributos Derivados")
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
    st.markdown(f"### Talentos de {char_sel}:")
    df_talentos = renderizar_talentos(p)
    st.table(df_talentos)

    st.divider()
    mostrar_equipamento(p)

    st.divider()
    mostrar_inventario(p)

    st.divider()
    
    st.header("Grimório & Forja Mágica")
    if p["Especializacao"] == "Conjuração":
        mostrar_grimorio_conjurador(p)
    elif p["Especializacao"] == "Invocação":
        mostrar_grimorio_invocador(p)
    elif p["Especializacao"] == "Magia Marcial":
        mostrar_grimorio_mago_marcial(p)
    else:
        st.info("Especialização indefinida. Não há seções adicionais para exibir.")

mostrar_ficha_daitai()