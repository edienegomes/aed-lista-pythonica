#Calcula a soma dos números de 1 até n.
def sum_numbers(n: int) -> int:
    soma = 0

    for i in range (1, n + 1):
        soma += i

    return soma
