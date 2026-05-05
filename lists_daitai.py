# lists_daitai.py

personagens_daitai = {
    "Zefiro Kruguel": {
        "Titulo": "O Açougueiro Infernal",
        "Raça": "Demônio",
        "Nivel": 6,
        "Elementos": ["Piro", "Metalo", "Umbra"],
        "Especializacao": "Conjuração",
        "Foto": "pp/zefiro.jpg",

        "Atributos": {
            "FOR": 7,
            "INT": 10,
            "DES": 6,
            "RES": 6,
            "VON": 9
        },

        "Pericias_Investidas": {
            "Atletismo": 0, 
            "Briga": 0,
            "Linguística": 1, 
            "Magia Teórica": 2, 
            "Natureza": 0,
            "Furtividade": 0, 
            "Pontaria": 2, 
            "Prestididitação": 0, 
            "Montaria": 0,
            "Fortitude": 0, 
            "Resiliência": 1, 
            "Recuperação": 0,
            "Liderança": 0, 
            "Intimidação": 0, 
            "Negociação": 0, 
            "Meditação": 0
        },

        "Talentos" : {
            "Fúria Demoníaca": " Ativável com <50% PV. Recebe +2 em FOR e INT, mas sofre −3 em RES.",
            "Catalizador de Mana": "O custo para todos os feitiços é reduzido em 10%.",
            "Persuasão Forte": "Você tem Vantagem (+1d6) em testes de perícias sociais ao interagir com pessoas de uma hierarquia social inferior."

        }
    },

    "Hugo Antonelli Roux": {
        "Titulo": "",
        "Raça": "Elfo",
        "Nivel": 6,
        "Elementos": ["Aero", "Electro", "Vibro","Hidro"],
        "Especializacao": "Conjuração",
        "Foto": "pp/hugo.jpg",

        "Atributos": {
            "FOR": 2,
            "INT": 14,
            "DES": 7,
            "RES": 6,
            "VON": 12
        },

        "Pericias_Investidas": {
            "Atletismo": 0, 
            "Briga": 0,
            "Linguística": 1, 
            "Magia Teórica": 2, 
            "Natureza": 1,
            "Furtividade": 0, 
            "Pontaria": 1, 
            "Prestididitação": 0, 
            "Montaria": 0,
            "Fortitude": 0, 
            "Resiliência": 1, 
            "Recuperação": 1,
            "Liderança": 0, 
            "Intimidação": 0, 
            "Negociação": 1, 
            "Meditação": 1
        },

        "Talentos" : {
            "Ventos Uivantes": "Uma vez ao dia, pode obter informações úteis do NR.",
            "Inteligência Aprimorada": "+2 em Inteligência",
            "Catalizador de Mana": "O custo para todos os feitiços é reduzido em 10%."
        }
    },

    "Nana": {
        "Titulo": "",
        "Raça": "Bestial",
        "Nivel": 3         ,
        "Elementos": ["Geo","Fito"],
        "Especializacao": "Magia Marcial",
        "Foto": "pp/nana.jpg",

        "Atributos": {
            "FOR": 10,
            "INT": 6,
            "DES": 8,
            "RES": 8,
            "VON": 6
        },

        "Pericias_Investidas": {
            "Atletismo": 1, 
            "Briga": 2,
            "Linguística": 0, 
            "Magia Teórica": 0, 
            "Natureza": 1,
            "Furtividade": 0, 
            "Pontaria": 0, 
            "Prestididitação": 0, 
            "Montaria": 0,
            "Fortitude": 2, 
            "Resiliência": 0, 
            "Recuperação": 0,
            "Liderança": 0, 
            "Intimidação": 0, 
            "Negociação": 0, 
            "Meditação": 0
        },

        "Talentos" : {
            "Instinto Selvagem": "Uma vez por descanso longo, pode ativar uma forma híbrida. Por um minuto, recebe +2 FOR e +2 DES e Vantagem em testes de Faro e Percepção.",
            "Natureza Primordial": "Sua forma mágica é inconstante. Ao rolar um 1 natural em um Teste de Habilidade, ele perde a concentração e sofre Desvantagem no próximo teste.",
            "Afinidade Espiritual": "Você tem Vantagem (+1d6) em testes que envolvam interações espirituais",
            "Atleta Arcano": "+2 em Destreza",
            "Força Aprimorada": "+2 em Força"
        }
    },

    "Lidane Kurogane": {
        "Titulo": "",
        "Raça": "Bestial",
        "Nivel": 7         ,
        "Elementos": ["Aero","Electro","Umbra","Piro"],
        "Especializacao": "Conjuração",
        "Foto": "pp/lidane.jpg",

        "Atributos": {
            "FOR": 8,
            "INT": 7,
            "DES": 10,
            "RES": 6,
            "VON": 6
        },

        "Pericias_Investidas": {
            "Atletismo": 3, 
            "Briga": 2,
            "Linguística": 1, 
            "Magia Teórica": 0, 
            "Natureza": 0,
            "Furtividade": 4, 
            "Pontaria": 0, 
            "Prestididitação": 0, 
            "Montaria": 0,
            "Fortitude": 1, 
            "Resiliência": 0, 
            "Recuperação": 0,
            "Liderança": 0, 
            "Intimidação": 0, 
            "Negociação": 0, 
            "Meditação": 0
        },

        "Talentos" : {
            "Instinto Selvagem": "Uma vez por descanso longo, pode ativar uma forma híbrida. Por um minuto, recebe +2 FOR e +2 DES e Vantagem em testes de Faro e Percepção.",
            "Natureza Primordial": "Sua forma mágica é inconstante. Ao rolar um 1 natural em um Teste de Habilidade, ele perde a concentração e sofre Desvantagem no próximo teste.",
            "Faro Apurado": "Tem um faro sensível, recebe vantagem em percepção usando o olfato.",
            "Foco na Batalha": "Quando está em combate direto (corpo a corpo), o Mago tem +1 em seu total de Pontos de Armadura (PA)."
        }
    },

     "Jade Rascki": {
        "Titulo": "",
        "Raça": "Vampiro",
        "Nivel": 3         ,
        "Elementos": ["Hidro", "Crio"],
        "Especializacao": "",
        "Foto": "pp/jade.jpg",

        "Atributos": {
            "FOR": 4,
            "INT": 10,
            "DES": 6,
            "RES": 5,
            "VON": 8
        },

        "Pericias_Investidas": {
            "Atletismo": 0, 
            "Briga": 0,
            "Linguística": 1, 
            "Magia Teórica": 3, 
            "Natureza": 0,
            "Furtividade": 0, 
            "Pontaria": 0, 
            "Prestididitação": 0, 
            "Montaria": 0,
            "Fortitude": 0, 
            "Resiliência": 0, 
            "Recuperação": 0,
            "Liderança": 1, 
            "Intimidação": 0, 
            "Negociação": 0, 
            "Meditação": 2
        },

        "Talentos" : {
            "Sede de Mana": "Uma vez por combate, ao causar dano a uma criatura viva, recupera 1d4 PM (Pontos de Mana).",
            "Fragilidade Solar": "Enquanto estiver sob luz solar direta, sofre Desvantagem em todos os Testes de Resistência e Vontade.",
            "Catalizador de Mana": "O custo para todos os feitiços é reduzido em 10%.",
            "Rastreador Mágico": "Tem vantagem em testes de detecção mágica"
        }
    }

    # "": {
    #     "Titulo": "",
    #     "Raça": "",
    #     "Nivel": 0         ,
    #     "Elementos": [""],
    #     "Especializacao": "",
    #     "Foto": "pp/.jpg",

    #     "Atributos": {
    #         "FOR": 10,
    #         "INT": 6,
    #         "DES": 8,
    #         "RES": 8,
    #         "VON": 6
    #     },

    #     "Pericias_Investidas": {
    #         "Atletismo": 0, 
    #         "Briga": 0,
    #         "Linguística": 0, 
    #         "Magia Teórica": 0, 
    #         "Natureza": 0,
    #         "Furtividade": 0, 
    #         "Pontaria": 0, 
    #         "Prestididitação": 0, 
    #         "Montaria": 0,
    #         "Fortitude": 0, 
    #         "Resiliência": 0, 
    #         "Recuperação": 0,
    #         "Liderança": 0, 
    #         "Intimidação": 0, 
    #         "Negociação": 0, 
    #         "Meditação": 0
    #     },

    #     "Talentos" : {
    #         "": ""
    #     }
    # }

}

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