def convertir(nombre):
    if nombre <= 3:
        return cas_symbole_plus_n_unites('', 0, nombre)

    if nombre == 4:
        return 'IV'

    if nombre <= 8:
        return cas_symbole_plus_n_unites('V', 5, nombre)

    if nombre == 9:
        return 'IX'

    if nombre <= 13:
        return cas_symbole_plus_n_unites('X', 10, nombre)

    if nombre == 14:
        return 'XIIV'

    if nombre == 15:
        return 'XV'

    raise Exception('Nombre non supporté')


def cas_symbole_plus_n_unites(symbole, valeur_symbole, nombre_arabe):
    return symbole + 'I' * (nombre_arabe - valeur_symbole)