#Substitui um convidado indisponível por outro.
def modify_guest_list(
    guests: list[str],
    unavailable: str,
    new_guest: str
) -> list[str]:
    
    posicao = guests.index(unavailable)
    guests[posicao] = new_guest

    return guests