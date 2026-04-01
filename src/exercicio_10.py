#Recebe uma lista de nomes e retorna uma nova lista com mensagens.
def greet_names(names: list[str]) -> list[str]:
    lista_names = []

    for name in names:
        lista_names.append(f"Hello, {name}!")

    return lista_names