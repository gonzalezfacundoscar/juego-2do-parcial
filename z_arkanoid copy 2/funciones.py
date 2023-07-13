import re
'''
validar entero con regex
retorna True si es entero
retorna False si no cumple
'''
def validar_entero_regex(numero)->bool:
    patron_regex = r"^[0-9]+$"
    numero = str(numero)

    if re.match(patron_regex, numero):
        return True
    else:
        return False
    
'''
validar cadena con regex
retorna True si es str
retorna false si no cumple
'''
def validar_letras_regex(cadena:str):
    patron_regex = r"^[a-zA-Z]+$"
    
    if re.match(patron_regex, cadena):
        return True
    else:
        return False