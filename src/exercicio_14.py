#Gera uma lista de números de 1 até n.
def generate_numbers(n: int) -> list[int]:
    lista = []

    for i in range (1, n + 1):
        lista.append(i)

    return lista