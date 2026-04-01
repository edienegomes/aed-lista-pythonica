#Retorne uma lista com os números ímpares até n.
def odd_numbers(n: int) -> list[int]:
    lista = []

    for i in range(1, n + 1):
        if i % 2 != 0:
            lista.append(i)
    return lista

