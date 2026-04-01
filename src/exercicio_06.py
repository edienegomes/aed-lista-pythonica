#Remove espaços em branco no início e no fim da string
def clean_name(name: str) -> str:
    nome = name

    return name.strip()