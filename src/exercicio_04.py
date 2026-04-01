#Retorna o nome em diferentes formatos: (lowercase, uppercase, titlecase)
# minúsculo, maiúsculo, capitalizado 
def format_name(name: str) -> tuple[str, str, str]:
    nome = name
    
    return (nome.lower(), nome.upper(), nome.capitalize())
