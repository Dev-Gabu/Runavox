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
    "Equipamento": "assets/ui/equipamento.png",
    "Consumivel": "assets/ui/consumivel.png",
    "Artefato": "assets/ui/artefato.png",
    "Material": "assets/ui/material.png",

    "Arma": "assets/ui/espada.png",
    "Capacete" : "assets/ui/capacete.png",
    "Peitoral": "assets/ui/armaduras.png",
    "Calça": "assets/ui/calca.png",
    "Bota": "assets/ui/bota.png",
    "Luva": "assets/ui/luva.png",
    "Capa": "assets/ui/capa.png",
    "Acessório": "assets/ui/anel.png",
    "Colar": "assets/ui/colar.png",
}

TABELA_ELEMENTOS = [
    "Neutro","Piro", "Hidro", "Geo", "Aero", "Electro", "Crio", "Fito", "Metalo", "Umbra", "Lumino", "Vibro", "Crystalo", "Chrono", "Cosmo", "Nether", "Aether", "Psycho"]

TABELA_MOD_INVOCACAO = [
    {
        "Modificador": "Reforço de Couro",
        "Descrição": "Aumenta permanentemente o PA da Invocação em +1.",
        "Custo": 2
    },
    {
        "Modificador": "Treinamento Físico",
        "Descrição": "Aumenta um atributo (FOR, RES ou DES) da Invocação em +1.",
        "Custo": 1
    },
    {
        "Modificador": "Aumentar Intelecto",
        "Descrição": "Aumenta um atributo (INT ou VON) da Invocação em +1.",
        "Custo": 1
    },
    {
        "Modificador": "Vínculo Profundo",
        "Descrição": "Aumenta o PV total da Invocação em +10.",
        "Custo": 1
    },
    {
        "Modificador": "Penetração",
        "Descrição": "Os ataques da Invocação ignoram 2 pontos de PA do alvo.",
        "Custo": 1
    }
],

TABELA_A_TIPO_FEITICO = [
    # Tipo: Dano Direto, Construção, Efeito/Condição, Movimentação, Suporte, Criação de Objeto, Informação, Transformação
    # Duração: Instantâneo, X Turnos, Concentração, Até o fim do combate, Permanente
    # Alcance: Pessoal, Curto, Médio, Longo, Indefinido

   {
    "Tipo": "Dano Direto",
    "Descrição": "Projétil causa dano direto.",
    "Dano": (2, 6),
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

TABELA_B_MOD_FEITICO = [
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
    "Modificador": "Dano Aumentado",
    "Descrição": "Aumenta 1 a categoria do dado na rolagem de dano ou efeito.",
    "Custo": +2
    },
    {
    "Modificador": "Multi-alvo",
    "Descrição": "Aumenta 1 a quantidade de alvos.",
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

TABELA_C_TIPO_HABILIDADE = [

    {
    "Tipo": "Golpe Direto",
    "Descrição": "Ataque físico (mordida, garra, pancada).",
    "Dano": (1, 8),
    "Duração": "Instantâneo",
    "Alcance": "Curto",
    "Complexidade": 1
   },
   {
    "Tipo": "Projétil Orgânico",
    "Descrição": "Disparo de espinhos, cuspe ácido ou penas.",
    "Dano": (1, 6),
    "Duração": "Instantâneo",
    "Alcance": "Médio",
    "Complexidade": 2
   },
   {
    "Tipo": "Efeito de Aura",
    "Descrição": "A criatura emana uma energia que afeta quem está ao redor.",
    "Dano": None,
    "Duração": "1 Turno.",
    "Alcance": "Curto",
    "Complexidade": 3
   },
   {
    "Tipo": "Controle",
    "Descrição": "Atordoar, derrubar ou prender o alvo (ex: teia ou mordida que trava).",
    "Dano": None,
    "Duração": "1 Turno.",
    "Alcance": "Curto",
    "Complexidade": 3
   },
   {
    "Tipo": "Defesa",
    "Descrição": "A criatura protege o Mago, absorvendo dano ou concedendo bônus de PA.",
    "Dano": None,
    "Duração": "1 Turno.",
    "Alcance": "Pessoal",
    "Complexidade": 2
   },
   {
    "Tipo": "Suporte",
    "Descrição": "A criatura cura o invocador em 5 + 1d6 de PV.",
    "Dano": None,
    "Duração": "1 Turno.",
    "Alcance": "Pessoal",
    "Complexidade": 2
   },
   {
    "Tipo": "Movimentação",
    "Descrição": "Salto, voo momentâneo ou investida que atravessa inimigos.",
    "Dano": None,
    "Duração": "Instantâneo",
    "Alcance": "Curto",
    "Complexidade": 1
   },
   {
    "Tipo": "Rugido/Grito",
    "Descrição": "Afeta o mental dos inimigos em área, causando Medo ou Desvantagem..",
    "Dano": None,
    "Duração": "1 Turno.",
    "Alcance": "Curto.",
    "Complexidade": 3
   },
   {
    "Tipo": "Mimetismo",
    "Descrição": "A criatura altera sua cor ou forma. Recebe -2 em um modificador e +4 em outros 2.",
    "Dano": None,
    "Duração": "1 Turno.",
    "Alcance": "Pessoal.",
    "Complexidade": 4
   },

]

TABELA_D_MOD_HABILIDADE = [
    {
    "Modificador": "Dano aumentado",
    "Descrição": "Adiciona um dano ao dano da habilidade.",
    "Custo": 1
    },
    {
    "Modificador": "Potência aumentada",
    "Descrição": "Aumenta em um o grau do dado de dano da habilidade.",
    "Custo": 3
    },
    {
    "Modificador": "Efeito",
    "Descrição": "Adiciona dano contínuo 1d4 por 2 turnos ao ataque.",
    "Custo": 2
    },
    {
    "Modificador": "Alcance Elástico",
    "Descrição": "Membros ou língua que esticam, aumentando o alcance em +1 estágio.",
    "Custo": 1
    },
    {
    "Modificador": "Multi-Ataque",
    "Descrição": "A criatura atinge dois alvos próximos com a mesma ação.",
    "Custo": 3
    },
    {
    "Modificador": "Ferocidade",
    "Descrição": "Aumenta o crítico da habilidade (Margem de crítico reduz em 2).",
    "Custo": 2
    },
    {
    "Modificador": "Simbiose",
    "Descrição": "Parte do dano causado pela habilidade cura a Invocação ou o Mago. Cura em 1/4 do dano causado.",
    "Custo": 3
    },
    {
    "Modificador": "Sacrifício",
    "Descrição": "A criatura perde 2 + 1d6 PV para aumentar o dano da técnica em +2 dados.",
    "Custo": -1
    },
    {
    "Modificador": "Instinto Selvagem",
    "Descrição": "A técnica só pode ser usada se a criatura estiver com menos de 50% de PV.",
    "Custo": -2
    },
    {
    "Modificador": "Lentidão Crônica",
    "Descrição": "A criatura perde sua próxima ação de movimento.",
    "Custo": -1
    }
]

TABELA_E_TIPO_FORMACAO = [

{
    "Tipo" : "Tanque/Pesado",
    "Descrição" : "Uma postura defensiva que prioriza resistência e controle de espaço.",
    "Beneficio" : "+4 Mod. RES e +2 PA.",
    "Maleficio" : "-3 Mod. DES e Lentidão.",
    "Custo" : "3"
},

{
    "Tipo" : "Duelista/Veloz",
    "Descrição" : "Uma postura ofensiva que prioriza velocidade e agilidade.",
    "Beneficio" : "+4 Mod. DES e +1 Ação de Movimento.",
    "Maleficio" : "-3 Mod. FOR e -2 PA.",
    "Custo" : "3"
},

{
    "Tipo" : "Brutamontes",
    "Descrição" : "Uma postura que prioriza força física e dano bruto.",
    "Beneficio" : "+4 Mod. FOR e +1 dado de dano físico",
    "Maleficio" : "-3 Mod. INT e Desvantagem em Defesa.",
    "Custo" : "3"
},
{
    "Tipo" : "Preciso",
    "Descrição" : "Uma postura que prioriza precisão e controle.",
    "Beneficio" : "+2 Mod. VON e +2 Mod. INT",
    "Maleficio" : "Reduz em um dado o dano de ataques corpo a corpo. (Mínimo 1)",
    "Custo" : "3"
}

]

TABELA_F_MOD_FORMACAO = [
    {
    "Modificador": "Reação Instintiva",
    "Descrição": "Permite realizar um contra-ataque físico se o inimigo falhar o ataque.",
    "Custo": "3"
    },
    {
    "Modificador": "Aura Elemental",
    "Descrição": "Inimigos que terminam o turno em alcance curto recebem 1d6 de dano elemental.",
    "Custo": "2"
    },
    {
    "Modificador": "Passo Leve",
    "Descrição": "O Mago ignora penalidades de terreno difícil enquanto na formação.",
    "Custo": "2"
    },
    {
    "Modificador": "Pele de Éter",
    "Descrição": "Recebe Resistência Mágica (Reduz dano mágico em valor igual ao mod. VON).",
    "Custo": "2"
    },
    {
    "Modificador": "Foco de Execução",
    "Descrição": "Aumenta a margem de Crítico em +1.",
    "Custo": "2"
    }

]

TABELA_G_TIPO_TECNICA = [
    {
    "Tipo": "Impacto Elemental",
    "Descrição": "Um golpe que detona energia elemental no contacto.",
    "Dano": (1, 8),
    "Alcance": "Curto",
    "Complexidade": 2
    },
    {
    "Tipo": "Investida",
    "Descrição": "O Mago move-se e ataca no mesmo movimento.",
    "Dano": (1, 6),
    "Alcance": "Médio (Linha)",
    "Complexidade": 3
    },
    {
    "Tipo": "Varredura de Área",
    "Descrição": "Um golpe circular (giro ou rasteira) que atinge todos em volta.",
    "Dano": (1, 4),
    "Alcance": "Curto (Círculo)",
    "Complexidade": 3
    },
    {
    "Tipo": "Projeção de Golpe",
    "Descrição": "O Mago soca o ar e envia uma onda de choque elemental.",
    "Dano": (1, 6),
    "Alcance": "Médio",
    "Complexidade": 3
    },
    {
    "Tipo": "Garra/Presa",
    "Descrição": "Um agarrão que infunde mana no alvo, imobilizando-o.",
    "Dano": (1, 4),
    "Alcance": "Curto",
    "Complexidade": 4
    }

]

TABELA_H_MOD_TECNICA = [
    {
        "'Modificador": "Alcance Estendido",
        "Descrição": "Aumenta o alcance da técnica em um estágio.",
        "Custo": "3"
    },
    {
        "'Modificador": "Golpe Carregado",
        "Descrição": "Aumenta em 1 a quantidade de dados bônus.",
        "Custo": "2"
    },
    {
        "Modificador": "Golpe Devastador",
        "Descrição": "Aumenta em 1 a Categoria dos dados Bônus.",
        "Custo": "3"
    },
    {
        "Modificador": "Impacto Penetrante",
        "Descrição": "O golpe ignora uma quantidade de PA igual ao Mod. de DES.",
        "Custo": "2"
    },
    {
        "Modificador": "Vibração Ressonante",
        "Descrição": "O alvo deve passar num teste de RES ou ficar Atordoado.",
        "Custo": "3"
    },
    {
        "Modificador": "Drenagem de Essência",
        "Descrição": "Metade do dano causado é convertido em cura para o Mago.",
        "Custo": "4"
    },
    {
        "Modificador": "Golpe em Cadeia",
        "Descrição": "Se o golpe finalizar um inimigo, o Mago recebe uma ação de ataque extra nesse turno.",
        "Custo": "2"
    },
    {
        "Modificador": "Velocidade da Luz",
        "Descrição": "A técnica pode ser usada como Ação Bónus em vez de uma Ação Padrão. Seu dano é reduzido pela metade.",
        "Custo": "3"
    },
    {
        "Modificador": "Desgaste Físico",
        "Descrição": "Aumenta o dano em +2 dados, mas o Mago recebe 1d8 de dano real.",
        "Custo": "-2"
    }

]