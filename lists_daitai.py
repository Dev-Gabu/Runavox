# lists_daitai.py

personagens_daitai = {
    "Zefiro Kruguel": {
        "Titulo": "O Açougueiro Infernal",
        "Nivel": 6,
        "Elementos": ["Piro", "Metalo", "Umbra"], # Nível 6 libera 2º Primário
        "Especializacao": "Conjuração",
        "Foto": "pp/zefiro.jpg",
        "Atributos": {
            "FOR": 8,
            "INT": 15,
            "DES": 10,
            "RES": 12,
            "VON": 14
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