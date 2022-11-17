def convertir(nombre):
    if nombre <= 3:
        return cas_symbole_plus_unite('', 0, nombre)

    if nombre == 4:
        return 'IV'

    if nombre <= 8:
        return cas_symbole_plus_unite('V', 5, nombre)

    if nombre == 9:
        return 'IX'

    if nombre <= 13:
        return cas_symbole_plus_unite('X', 10, nombre)

    if nombre == 14:
        return 'XIV'

    if nombre == 15:
        return 'XV'

    raise Exception('Nombre non supporté')


def cas_symbole_plus_unite(symbole, valeur_symbole, nombre_arabe):
    return symbole + 'I' * (nombre_arabe - valeur_symbole)