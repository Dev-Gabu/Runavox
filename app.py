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
    
    aba1, aba2= st.tabs(["Invocações", "Criar Habilidade"])
    
    with aba1:
        grimorio = p.get("Grimorio", [])
        
        if not grimorio:
            st.info("Este mago ainda não transcreveu feitiços.")
        else:
            for invocacao in grimorio:
                with st.expander(f"🦉 {invocacao['Nome']} | PV: {invocacao['PV']} | PA: {invocacao['PA']})"):
                    st.image(invocacao['Aparencia'], width=150)
                    st.write(f"**Descricao:** {invocacao['Descricao']}")
                    st.write(f"**Categoria:** {invocacao['Categoria']}")
                    st.write(f"**Elemento:** {invocacao['Elemento']}")
                    st.write(f"**Dano:** {invocacao['Dano fixo']} + {invocacao['Dano dado'][0]}d{invocacao['Dano dado'][1]}")
                    
                    st.write("**== Atributos e Modificadores ==**")
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

                    with st.expander("💢 Habilidades da Invocação"):
                        for habilidade in invocacao.get("Habilidades", []):
                            with st.expander(f"✨ {habilidade['Nome']} (Custo: {habilidade['Custo']} PM)"):
                                st.write(f"**Descrição:** {habilidade['Descrição']}")
                                if habilidade['Dano'] is not None: st.write(f"**Dano:** {habilidade['Dano'][0]}d{habilidade['Dano'][1]}")
                                if habilidade['Alcance'] is not None: st.write(f"**Alcance:** {habilidade['Alcance'] }")
                                if habilidade['Duração'] is not None: st.write(f"**Duração:** {habilidade['Duração'] }")

    with aba2:
        st.subheader("Criar Habilidade")

        st.markdown("Molda a essência e as técnicas de combate das criaturas através do grimório.")

        at_personagem = p.get("Atributos", {"VON": 6})
        mod_von = get_mod(at_personagem.get("VON", 6))
        nivel_atual = p.get("Nivel", 1)
        lc_limite = nivel_atual + mod_von 
        
        st.write(f"**Nível:** {nivel_atual} | **Modificador de VON:** {mod_von}")
        st.info(f"🔮 Seu **Limite de Complexidade (LC)** para criar habilidades é: **{lc_limite}**")

        st.markdown("---")
        
        # --- PASSO 1: SELEÇÃO DA HABILIDADE BASE ---
        st.subheader("Definir a Habilidade Base")
        opcoes_habilidades = [h["Tipo"] for h in TABELA_C_TIPO_HABILIDADE]
        tipo_selecionado = st.selectbox("Selecione o tipo da habilidade:", opcoes_habilidades)
        
        # Encontra os dados da habilidade escolhida
        hab_base = next(h for h in TABELA_C_TIPO_HABILIDADE if h["Tipo"] == tipo_selecionado)
        st.caption(f"ℹ️ {hab_base['Descrição']}")
        comp_base = hab_base["Complexidade"]

        st.markdown("---")

        # --- PASSO 2: APLICAÇÃO DE MODIFICADORES ---
        st.subheader("Aplicar Modificadores")
        st.write("Marque as alterações que deseja aplicar à habilidade base:")
        
        modificadores_escolhidos = []
        comp_modificadores = 0
        
        # Renderiza os modificadores em formato de checkboxes funcionais
        for mod in TABELA_D_MOD_HABILIDADE:
            sinal = "+" if mod["Custo"] >= 0 else ""
            label_checkbox = f"{mod['Modificador']} ({sinal}{mod['Custo']} LC) — {mod['Descrição']}"
            
            if st.checkbox(label_checkbox, key=f"mod_inv_{mod['Modificador']}"):
                modificadores_escolhidos.append(mod["Modificador"])
                comp_modificadores += mod["Custo"]

        st.markdown("---")

        # --- CÁLCULO E VALIDAÇÃO FINAL ---
        st.subheader("✒️ Resumo e Validação da Habilidade")
        
        nome_tecnica = st.text_input("Dê um nome para a habilidade:", placeholder="Ex: Mordida de Titânio")
        complexidade_total = comp_base + comp_modificadores
        custo_mana = max(5, complexidade_total * 5) # Garante um custo mínimo caso os nerfs zerem o valor
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Complexidade da Base", f"{comp_base} LC")
        col2.metric("Complexidade Total", f"{complexidade_total} / {lc_limite} LC")
        col3.metric("Custo de Mana (PM)", f"{custo_mana} PM")

        if complexidade_total > lc_limite:
            st.error(f"❌ **Habilidade Inválida!** A complexidade calculada ({complexidade_total}) ultrapassa o limite de sua Vontade atual ({lc_limite}).")
        else:
            st.success(f"✅ **Habilidade Aprovada!** Habilidade pronta para ser transcrita nas suas Páginas de Grimório.")
            
            ## Atualizar os modificadores
            ## Adicionando efeitos aos modificadores
            # for mod in modificadores_escolhidos:
            #     if mod["Modificador"] == "Alcance Elástico":
            #         if hab_base["Alcance"] is not None and hab_base["Alcance"] != "Pessoal":
            #             hab_base["Alcance"] = "Longo" if hab_base["Alcance"] == "Médio" else "Médio"
            #     elif mod["Modificador"] == "Sacrifício":
            #         hab_base["Dano"] = (hab_base["Dano"][0] + 1, hab_base["Dano"][1]) if hab_base["Dano"] else None
            #     elif mod["Modificador"] == "Dano Aumentado":
            #         hab_base["Dano"] = (hab_base["Dano"][0] + 1, hab_base["Dano"][1]) if hab_base["Dano"] else None
            #     elif mod["Modificador"] == "Potência aumentada":
            #         hab_base["Dano"] = (hab_base["Dano"][0], hab_base["Dano"][1] + 2 if hab_base["Dano"] < 12 else hab_base["Dano"][1] + 8) if hab_base["Dano"] else None

            objeto_habilidade = {
                "Nome": nome_tecnica if nome_tecnica else tipo_selecionado,
                "Tipo": tipo_selecionado,
                "Descrição": "".join([hab_base["Descrição"]] + [mod["Descrição"] for mod in TABELA_D_MOD_HABILIDADE if mod["Modificador"] in modificadores_escolhidos]),
                "Dano": hab_base["Dano"] if hab_base["Dano"] else None,
                "Duração": hab_base["Duração"] if hab_base["Duração"] else None,
                "Alcance": hab_base["Alcance"] if hab_base["Alcance"] else None,
                "Complexidade": complexidade_total,
                "Custo": custo_mana
            }
            
            st.json(objeto_habilidade)        

def mostrar_grimorio_mago_marcial(p):

    aba1, aba2 = st.tabs(["Ver Grimório Marcial", "Criar Nova Técnica"])
    
    with aba1:
        st.subheader(f"Técnicas Conhecidas")
        grimorio = p.get("Grimorio", [])
        
        if not grimorio:
            st.info("Este mago ainda não transcreveu técnicas.")
        else:
            for spell in grimorio:
                if spell['Categoria'] == "tecnica":
                    with st.expander(f"🥊 {spell['Nome']} (Comp: {spell['Complexidade']} | PM: {spell['Mana']})"):
                        st.write(f"**Tipo:** {spell['Tipo']}")
                        st.write(f"**Custo:** {spell['Mana']} PM")
                        st.write(f"**Elemento:** {spell['Elemento']}")
                        st.write(f"---")
                        st.write(spell['Descrição'])
                        if spell['Dano']  is not None: st.write(f"**Dano:** {spell['Dano'][0]}d{spell['Dano'][1]}")
                        if spell['Alcance'] is not None: st.write(f"**Alcance:** {spell['Alcance'] }")
                        if spell['Duração'] is not None: st.write(f"**Duração:** {spell['Duração'] }")

                elif spell['Categoria'] == "formacao":
                    with st.expander(f"🥋 {spell['Nome']} (Comp: {spell['Complexidade']} | PM: {spell['Mana']})"):
                        st.write(f"**Tipo de Postura:** {spell['Tipo']}")
                        st.write(f"**Elemento:** {spell['Elemento']}")
                        st.write(f"---")
                        st.write(spell['Descrição'])
                        st.write(f"Melhoria: {spell['Buff'] if 'Buff' in spell else 'Nenhum'}")
                        st.write(f"Penalidade: {spell['Debuff'] if 'Debuff' in spell else 'Nenhum'}")

    with aba2:

        at_personagem = p.get("Atributos", {"RES": 6})
        mod_res = get_mod(at_personagem.get("RES", 6))
        nivel_atual = p.get("Nivel", 1)
        lc_limite = nivel_atual + mod_res 
        
        st.write(f"**Nível:** {nivel_atual} | **Modificador de RES:** {mod_res}")
        st.info(f"🛡️ Seu **Limite de Complexidade (LC)** para Magia Marcial é: **{lc_limite}**")

        sub_aba_formacao, sub_aba_tecnica = st.tabs(["🥋 Criar Formação", "👊 Criar Técnica"])
       
        with sub_aba_formacao:
            st.subheader("Passo 1: Definir o Arquétipo da Formação")
            opcoes_formacao = [f["Tipo"] for f in TABELA_E_TIPO_FORMACAO]
            formacao_sel = st.selectbox("Escolha a postura base do seu corpo:", opcoes_formacao)
            
            f_base = next(f for f in TABELA_E_TIPO_FORMACAO if f["Tipo"] == formacao_sel)
            st.caption(f"ℹ️ *{f_base['Descrição']}*")
            
            # Exibição limpa de bônus e penalidades do arquétipo
            col_f1, col_f2 = st.columns(2)
            col_f1.success(f"**Bônus:** {f_base['Beneficio']}")
            col_f2.error(f"**Penalidade:** {f_base['Maleficio']}")

            elemento_formacao = st.selectbox("Selecionar elemento da formação:", ["Neutro"] + TABELA_ELEMENTOS, key="elem_form_marcial")

            comp_f_base = int(f_base["Custo"])

            st.markdown("---")
            st.subheader("Passo 2: Aplicar Modificadores de Postura")
            
            mods_f_escolhidos = []
            comp_f_mods = 0
            descricao_mods = ""

            for mod in TABELA_F_MOD_FORMACAO:
                # Tratamento caso o custo venha como string com sinal "+3" ou "-2"
                custo_limpo = int(mod["Custo"].replace("+", "").strip())
                label = f"{mod['Modificador']} (+{custo_limpo} LC) — {mod['Descrição']}"
                
                if st.checkbox(label, key=f"form_mod_{mod['Modificador']}"):
                    mods_f_escolhidos.append(mod["Modificador"])
                    comp_f_mods += custo_limpo
                    descricao_mods += f"{mod['Descrição']} "


            st.markdown("---")
            st.subheader("✒️ Selar Formação Elemental")
            nome_formacao = st.text_input("Nome da Formação (Ex: Postura do Titã de Pedra)", key="input_nome_form")
            
            total_lc_f = comp_f_base + comp_f_mods
            pm_f = total_lc_f * 5

            c1, c2, c3 = st.columns(3)
            c1.metric("Complexidade Base", f"{comp_f_base} LC")
            c2.metric("Complexidade Final", f"{total_lc_f} / {lc_limite} LC")
            c3.metric("Custo para Ativar", f"{pm_f} PM")

            if total_lc_f > lc_limite:
                st.error(f"❌ **Formação Inválida!** A complexidade ({total_lc_f}) excede seu limite de RES ({lc_limite}).")
            else:
                st.success("✅ **Formação aprovada!** Pronta para ser assumida em combate.")
                objeto_formacao = {
                    
                    "Categoria": "formacao",
                    "Nome" : nome_formacao if nome_formacao else formacao_sel,
                    "Elemento": elemento_formacao,
                    "Tipo": formacao_sel,
                    "Descrição": descricao_mods.strip() if descricao_mods else f_base["Descrição"],
                    "Buff": f_base["Beneficio"],
                    "Debuff": f_base["Maleficio"],
                    "Complexidade": total_lc_f,
                    "Custo": pm_f
                }
                st.json(objeto_formacao)

        with sub_aba_tecnica:
            st.subheader("Passo 1: Definir o Estilo de Golpe")
            opcoes_tecnica = [t["Tipo"] for t in TABELA_G_TIPO_TECNICA]
            tecnica_sel = st.selectbox("Escolha o ataque físico condutor de mana:", opcoes_tecnica)
            
            t_base = next(t for t in TABELA_G_TIPO_TECNICA if t["Tipo"] == tecnica_sel)
            st.caption(f"ℹ️ *{t_base['Descrição']}*")
            
            col_t1, col_t2 = st.columns(2)
            col_t1.metric("Dano Inicial da Técnica", f"{t_base['Dano'][0]}d{t_base['Dano'][1]}")
            col_t2.metric("Alcance Padrão", t_base["Alcance"])
            
            comp_t_base = t_base["Complexidade"]

            elemento_tecnica = st.selectbox("Selecionar elemento da tecnica:", ["Neutro"] + TABELA_ELEMENTOS, key="elem_tecn_marcial")

            st.markdown("---")
            st.subheader("Passo 2: Aplicar Modificadores de Impacto")
            
            mods_t_escolhidos = []
            comp_t_mods = 0
            
            for mod in TABELA_H_MOD_TECNICA:
                # Correção para o erro de digitação do caractere "'Modificador" contido na lista bruta
                chave_mod = "Modificador" if "Modificador" in mod else "'Modificador"
                nome_mod = mod[chave_mod]
                
                custo_limpo = int(mod["Custo"].replace("+", "").strip())
                sinal = "+" if custo_limpo >= 0 else ""
                label = f"{nome_mod} ({sinal}{mod['Custo']} LC) — {mod['Descrição']}"
                
                if st.checkbox(label, key=f"tec_mod_{nome_mod}"):
                    mods_t_escolhidos.append(nome_mod)
                    comp_t_mods += custo_limpo
                    descricao_mods += f"{mod['Descrição']} "

                    if nome_mod == "Alcance Estendido":
                        if t_base["Alcance"] == "Corpo a Corpo":
                            t_base["Alcance"] = "Curto"
                        elif t_base["Alcance"] == "Curto":
                            t_base["Alcance"] = "Médio"
                        elif t_base["Alcance"] == "Médio":
                            t_base["Alcance"] = "Longo"
                    elif nome_mod == "Golpe Carregado":
                        t_base["Dano"] = (t_base["Dano"][0] + 1, t_base["Dano"][1]) if t_base["Dano"] else None
                    elif nome_mod == "Golpe Devastador":
                        t_base["Dano"] = (t_base["Dano"][0], t_base["Dano"][1] + 2 if t_base["Dano"][1] < 12 else t_base["Dano"][1] + 8) if t_base["Dano"] else None

            st.markdown("---")
            st.subheader("✒️ Transcrever Técnica no Grimório")
            nome_tecnica = st.text_input("Nome da Técnica (Ex: Impacto Relâmpago de Electro)", key="input_nome_tec")
            
            total_lc_t = comp_t_base + comp_t_mods
            pm_t = max(5, total_lc_t * 5)

            ct1, ct2, ct3 = st.columns(3)
            ct1.metric("Complexidade Base", f"{comp_t_base} LC")
            ct2.metric("Complexidade Final", f"{total_lc_t} / {lc_limite} LC")
            ct3.metric("Custo de Execução", f"{pm_t} PM")

            if total_lc_t > lc_limite:
                st.error(f"❌ **Técnica Inválida!** A complexidade ({total_lc_t}) excede seu limite de RES ({lc_limite}).")
            else:
                st.success("✅ **Técnica aprovada!** Pronta para ser desferida na linha de frente.")
                objeto_tecnica = {
                        "Categoria": "tecnica",
                        "Nome": nome_tecnica if nome_tecnica else tecnica_sel,
                        "Elemento": elemento_tecnica,
                        "Tipo": tecnica_sel,
                        "Descrição": descricao_mods.strip() if descricao_mods else t_base["Descrição"],
                        "Dano": t_base["Dano"] if t_base["Dano"] else None,
                        "Alcance": t_base["Alcance"] if t_base["Alcance"] else "Curto",
                        "Complexidade": total_lc_t,
                        "Custo_Mana_PM": pm_t
                    }
                
                st.json(objeto_tecnica)

## PÁGINA PRINCIPAL
def mostrar_ficha_daitai():
    st.title("RUNAVOX")
    st.title("O sistema integrado de Daitai Sunpo")
    st.divider()
    
    abas_principais = st.tabs(["Personagens", "Bestiário", "Loja", "Biblioteca"])

    with abas_principais[0]: #Personagens

        st.title("Ficha de Personagem")
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
        
        abas = st.tabs(["Atributos", "Inventário","Equipamento", "Grimório","Forja"])

        # Aba de Atributos
        with abas[0]:

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

            st.markdown("### Habilidade de Classe")
            if p["Especializacao"] == "Conjuração":
                st.markdown("Versatilidade Mágica: Uma vez por sessão de estudo, o Conjurador pode modificar temporariamente (sem gastar PMF) um Feitiço Base de seu Grimório, trocando um de seus Modificadores de Complexidade por outro.")
            elif p["Especializacao"] == "Invocação":
                st.markdown("Vínculo Compartilhado: O Invocador pode gastar uma ação de movimento e 30 Pontos de Mana (PM) para conceder uma Ação extra a uma de suas Invocações durante o turno dela.")
            elif p["Especializacao"] == "Magia Marcial":
                st.markdown("Canalização Corporal: Uma vez por turno, o Mago Marcial pode usar Mana para aumentar o dano de um ataque físico bem-sucedido em +1d6 (Custo: 10 PM).")
        # Aba de Inventário
        with abas[1]:
            mostrar_inventario(p)
        # Aba de Equipamento
        with abas[2]:
            mostrar_equipamento(p)
        # Aba de Grimório
        with abas[3]:
            st.header("Grimório & Forja Mágica")
            if p["Especializacao"] == "Conjuração":
                mostrar_grimorio_conjurador(p)
            elif p["Especializacao"] == "Invocação":
                mostrar_grimorio_invocador(p)
            elif p["Especializacao"] == "Magia Marcial":
                mostrar_grimorio_mago_marcial(p)
            else:
                st.info("Especialização indefinida. Não há seções adicionais para exibir.")
        # Aba de Forja
        with abas[4]:
                st.info("A seção de Forja ainda está em desenvolvimento. Fique atento para futuras atualizações!")

    with abas_principais[1]: #Bestiário
        st.title("Bestiário")
        st.info("Aqui estão listadas as criaturas e monstros que habitam o mundo de Daitai Sunpo e o Terreno Paralelo, com todos os dados de acesso público e/ou restritos aos alunos de classe especial da academia. Cada entrada inclui informações sobre suas características, habilidades e fraquezas, para ajudar os aventureiros a se prepararem para os encontros que terão pela frente!")

        st.divider()

        st.markdown("**Criaturas de Zenestria**")

        ## Adicionar a lista de criaturas

        st.divider()
        
        st.markdown("**Criaturas do Terreno Paralelo**")
        locais = st.tabs(["Gaia","Eris","Moira","Interios","Nebulus","Infernus"])

    with abas_principais[2]: #Loja
        st.info("A Loja de Daitai Sunpo está sendo preparada. Em breve, um espaço para adquirir itens mágicos, equipamentos e recursos para suas aventuras!")
    
    with abas_principais[3]: #Biblioteca
        st.info("A Biblioteca de Daitai Sunpo está em fase de desenvolvimento. Em breve, um acervo de livros, grimórios e conhecimentos para expandir o universo do jogo!")
mostrar_ficha_daitai()