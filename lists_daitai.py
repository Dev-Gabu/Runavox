# lists_daitai.py

personagens_daitai = {
    "Zefiro Kruguel": {
        "Titulo": "O Açougueiro Infernal",
        "Raça": "Demônio",
        "Nivel": 6,
        "Elementos": ["Piro", "Metalo", "Umbra"], # Nível 6 libera 2º Primário
        "Especializacao": "Conjuração",
        "Foto": "pp/zefiro.jpg",

        "Atributos": {
            "FOR": 6,
            "INT": 8,
            "DES": 6,
            "RES": 6,
            "VON": 9
        },

        "Pericias_Investidas": {
            "Atletismo": "0", 
            "Briga": "0",
            "Linguística": "1", 
            "Magia Teórica": "2", 
            "Natureza": "0",
            "Furtividade": "0", 
            "Pontaria": "2", 
            "Prestididitação": "0", 
            "Montaria": "0",
            "Fortitude": "0", 
            "Resiliência": "1", 
            "Recuperação": "0",
            "Liderança": "0", 
            "Intimidação": "0", 
            "Negociação": "0", 
            "Meditação": "0"
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