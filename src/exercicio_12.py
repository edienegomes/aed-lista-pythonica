#Adiciona múltiplos convidados à lista.
def add_guests(
    guests: list[str],
    new_guests: list[str]
) -> list[str]:
    
    total_lista = guests + new_guests 

    return total_lista
