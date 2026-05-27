import streamlit as st
import json
import os

PASTA_PERSONAGENS = "data/personagens"

@st.cache_data
def carregar_nomes_personagens():
    """Lê a pasta e retorna uma lista com os nomes dos arquivos/personagens."""
    if not os.path.exists(PASTA_PERSONAGENS):
        os.makedirs(PASTA_PERSONAGENS)
    
    arquivos = [f for f in os.listdir(PASTA_PERSONAGENS) if f.endswith(".json")]
    return arquivos

def carregar_ficha_individual(nome_arquivo):
    """Carrega o arquivo JSON específico de um personagem."""
    caminho = os.path.join(PASTA_PERSONAGENS, nome_arquivo)
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_ficha_individual(nome_arquivo, dados_atualizados):
    """Grava as alterações no arquivo e limpa o cache do Streamlit."""
    caminho = os.path.join(PASTA_PERSONAGENS, nome_arquivo)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados_atualizados, f, indent=4, ensure_ascii=False)
    
    st.cache_data.clear()


def renderizar_pagina_admin():
    st.title("Painel do Mestre - Editor de Fichas")

    lista_arquivos = carregar_nomes_personagens()

    if not lista_arquivos:
        st.warning("Nenhum personagem encontrado na pasta 'data/personagens/'. Crie um arquivo .json para começar.")
        if st.button("Criar Personagem Modelo (Zefiro)"):
            modelo = {
                "Nome": "Zefiro Kruguel",
                "Elemento": "Aero",
                "Nivel": 1,
                "Atributos": {"FOR": 10, "RES": 10, "INT": 10, "DES": 10, "VON": 10},
                "Historia": "Um jovem aspirante da academia Daitai Sunpo..."
            }
            salvar_ficha_individual("zefiro_kruguel.json", modelo)
            st.rerun()
        return

    # Passo 1: Seleção do Personagem
    arquivo_selecionado = st.selectbox(
        "Selecione o Personagem para Editar:", 
        options=lista_arquivos,
        format_func=lambda x: x.replace(".json", "").replace("_", " ").title()
    )

    # Carrega os dados atuais do personagem selecionado
    # Usamos o st.session_state para garantir a estabilidade dos dados enquanto editamos
    ficha = carregar_ficha_individual(arquivo_selecionado)

    st.divider()
    st.subheader(f"Editando: {ficha.get('Nome', 'Sem Nome')}")

    # Passo 2: Formulário de Edição (Agrupado por seções)
    with st.form("form_editor_personagem"):
        col1, col2 = st.columns(2)
        
        with col1:
            novo_nome = st.text_input("Nome do Personagem:", value=ficha.get("Nome", ""))
            novo_elemento = st.selectbox(
                "Elemento Principal:", 
                options=["Piro", "Hidro", "Aero", "Geo", "Metalo", "Eletro", "Luz", "Trevas"],
                index=["Piro", "Hidro", "Aero", "Geo", "Metalo", "Eletro", "Luz", "Trevas"].index(ficha.get("Elemento", "Piro"))
            )
        
        with col2:
            novo_nivel = st.number_input("Nível:", min_value=1, max_value=20, value=int(ficha.get("Nivel", 1)))

        # Edição de Atributos Dinâmicos
        st.write("### ⚔️ Atributos Básicos")
        atributos_atuais = ficha.get("Atributos", {"FOR": 0, "RES": 0, "INT": 0, "DES": 0, "VON": 0})
        
        col_at1, col_at2, col_at3, col_at4, col_at5 = st.columns(5)
        with col_at1:
            nova_for = st.number_input("FOR", value=int(atributos_atuais.get("FOR", 0)))
        with col_at2:
            nova_res = st.number_input("RES", value=int(atributos_atuais.get("RES", 0)))
        with col_at3:
            nova_int = st.number_input("INT", value=int(atributos_atuais.get("INT", 0)))
        with col_at4:
            nova_des = st.number_input("DES", value=int(atributos_atuais.get("DES", 0)))
        with col_at5:
            nova_von = st.number_input("VON", value=int(atributos_atuais.get("VON", 0)))

        # Campos de texto longa (Ex: História ou Notas do Mestre)
        nova_historia = st.text_area("História / Descrição do Personagem:", value=ficha.get("Historia", ""))

        # Passo 3: Botão de Salvar (Dentro do formulário)
        botao_salvar = st.form_submit_button("Salvar Alterações")

        if botao_salvar:
            # Monta o novo dicionário estruturado
            dados_atualizados = {
                "Nome": novo_nome,
                "Elemento": novo_elemento,
                "Nivel": novo_nivel,
                "Atributos": {
                    "FOR": nova_for,
                    "RES": nova_res,
                    "INT": nova_int,
                    "DES": nova_des,
                    "VON": nova_von
                },
                "Historia": nova_historia
            }

            # Executa a gravação física no arquivo
            salvar_ficha_individual(arquivo_selecionado, dados_atualizados)
            st.success(f"Ficha de {novo_nome} atualizada com sucesso no arquivo local!")
            
            # Recarrega a página para atualizar as listagens visuais imediatamente
            st.rerun()

# Para testar diretamente:
if __name__ == "__main__":
    renderizar_pagina_admin()