def get_rank(nivel):
    if nivel >= 12: return "Rank A/S"
    if nivel >= 9: return "Rank B"
    if nivel >= 6: return "Rank C"
    if nivel >= 3: return "Rank D"
    return "Rank E"

def get_mod(valor):
    # Cálculo oficial: (A-6)/2 arredondado
    return (valor - 6) // 2

MAPA_PERICIAS = {
    "Atletismo": "FOR", "Briga": "FOR",
    "Linguística": "INT", "Magia Teórica": "INT", "Natureza": "INT",
    "Furtividade": "DES", "Pontaria": "DES", "Prestididitação": "DES", "Montaria": "DES",
    "Fortitude": "RES", "Resiliência": "RES", "Recuperação": "RES",
    "Liderança": "VON", "Intimidação": "VON", "Negociação": "VON", "Meditação": "VON"
}

ICON_MAP = {
    "Equipamento": "assets/equipamento.png",
    "Consumivel": "assets/consumivel.png",
    "Artefato": "assets/artefato.png",
    "Material": "assets/material.png",

    "Arma": "assets/espada.png",
    "Capacete" : "assets/capacete.png",
    "Peitoral": "assets/armaduras.png",
    "Calça": "assets/calca.png",
    "Bota": "assets/bota.png",
    "Luva": "assets/luva.png",
    "Capa": "assets/capa.png",
    "Acessório": "assets/anel.png",
    "Colar": "assets/colar.png",
}

TABELA_ELEMENTOS = [
    "Neutro","Piro", "Hidro", "Geo", "Aero", "Electro", "Crio", "Fito", "Metalo", "Umbra", "Lumino", "Vibro", "Crystalo", "Chrono", "Cosmo", "Nether", "Aether", "Psycho"]

TABELA_A_TIPOS = [
    # Tipo: Dano Direto, Construção, Efeito/Condição, Movimentação, Suporte, Criação de Objeto, Informação, Transformação
    # Duração: Instantâneo, X Turnos, Concentração, Até o fim do combate, Permanente
    # Alcance: Pessoal, Curto, Médio, Longo, Indefinido

   {
    "Tipo": "Dano Direto",
    "Descrição": "Projétil focado em um único alvo. Causa 2d6 de dano.",
    "Dano": "2d6",
    "Duração": "Instantâneo",
    "Alcance": "Curto",
    "Complexidade": 2
   },
   {
    "Tipo": "Construção",
    "Descrição": "Cria uma estrutura ou área fixa. ",
    "Dano": None,
    "Duração": "1 Turno por modificador de RES.",
    "Alcance": "Curto",
    "Complexidade": 3
   },
   {
    "Tipo": "Efeito / Condição",
    "Descrição": "Causa dano por turno ou impõe uma condição.",
    "Dano": None,
    "Duração": "1 Turno.",
    "Alcance": "Curto",
    "Complexidade": 3
   },
   {
    "Tipo": "Movimentação",
    "Descrição": "Impulsiona o mago ou alvo.",
    "Dano": None,
    "Duração": "Instantâneo",
    "Alcance": "Curto",
    "Complexidade": 2
   },
   {
    "Tipo": "Suporte",
    "Descrição": "Cura, concede bônus temporário. ",
    "Dano": None,
    "Duração": "1 Turno.",
    "Alcance": "Curto",
    "Complexidade": 3
   },
   {
    "Tipo": "Criação de Objeto",
    "Descrição": "Cria uma arma, armadura ou ferramenta simples.",
    "Dano": None,
    "Duração": "1 minuto.",
    "Alcance": "Curto",
    "Complexidade": 4
   },
   {
    "Tipo": "Informação",
    "Descrição": "Concede percepção além do normal.",
    "Dano": None,
    "Duração": "1 minuto.",
    "Alcance": "Pessoal",
    "Complexidade": 2
   },
   {
    "Tipo": "Transformação",
    "Descrição": "Altera a forma do Mago ou de um objeto.",
    "Dano": None,
    "Duração": "1 Turno.",
    "Alcance": "Pessoal",
    "Complexidade": 5
   }

]

TABELA_B_MODS = [
    {
    "Modificador": "Alcance Aumentado",
    "Descrição": "Aumenta o alcance do feitiço em um nível (Pessoal → Curto → Médio ou Médio → Longo). Pode ser aplicado várias vezes.",
    "Custo": +1
    },
    {
    "Modificador": "Área de Efeito (AoE)",
    "Descrição": "Transforma o feitiço de alvo único em um ataque de área ou aumenta a área de efeito em um estágio (Curto → Médio ou Médio → Longo). Pode ser aplicado várias vezes.",
    "Custo": +2
    },
    {
    "Modificador": "Duração Aumentada",
    "Descrição": "Aumenta em 1 turno a duração padrão. Pode ser aplicado várias vezes.",
    "Custo": +1
    },
    {
    "Modificador": "Confiabilidade",
    "Descrição": "CD para resistir ao efeito do feitiço aumenta em +2.",
    "Custo": +1
    },
    {
    "Modificador": "Potência Melhorada",
    "Descrição": "Aumenta 1 dado na rolagem de dano ou efeito. Pode ser aplicado várias vezes.",
    "Custo": +2
    },
    {
    "Modificador": "Feitiço Sustentado",
    "Descrição": "O mago deve gastar sua Ação Completa para manter o feitiço ativo. Apenas em feitiços com duração.",
    "Custo": -1
    },
    {
    "Modificador": "Requer Preparo",
    "Descrição": "Mago deve gastar sua Ação de Preparar para conjurar o feitiço no turno seguinte.",
    "Custo": -1
    },
    {
    "Modificador": "Efeito Secundário",
    "Descrição": "Adiciona um efeito ou condição secundária, exige um teste de resistência.",
    "Custo": +3
    }
]






