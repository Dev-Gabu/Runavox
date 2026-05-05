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
    }
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