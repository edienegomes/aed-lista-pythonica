#Retorna uma frase com autor e citação
def famous_quote(author: str, quote: str) -> str:
    nome = author
    citacao = quote

    return f"{nome} once said, '{citacao}'"