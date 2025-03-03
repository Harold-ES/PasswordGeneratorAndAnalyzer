# password_analyzer.py


import math

# Calcular la entropia
def calcular_entropia(password):
    conjuntos = 0
    if any(c.islower() for c in password): conjuntos += 26
    if any(c.isupper() for c in password): conjuntos += 26
    if any(c.isdigit() for c in password): conjuntos += 10
    if any(c in "!@#$%^&*()-_=+[]{};:'\",.<>?/`~" for c in password): conjuntos += 32

    if conjuntos == 0:
        return 0

    entropia = len(password) * math.log2(conjuntos)
    return entropia

def clasificar_seguridad(entropia):
    if entropia < 40:
        return "Muy débil"
    elif entropia < 60:
        return "Débil"
    elif entropia < 80:
        return "Moderada"
    elif entropia < 100:
        return "Fuerte"
    else:
        return "Muy fuerte"

def generar_recomendaciones(password, entropia):
    recomendaciones = []
    
    if entropia < 40:
        recomendaciones.append("Use una contraseña más larga (mínimo 12 caracteres).")
        recomendaciones.append("Incluya letras mayúsculas, números y símbolos.")
    elif entropia < 60:
        if not any(c.isupper() for c in password):
            recomendaciones.append("Agrege al menos una letra mayúscula.")
        if not any(c.isdigit() for c in password):
            recomendaciones.append("Incluya al menos un número.")
        if not any(c in "!@#$%^&*()-_=+[]{};:'\",.<>?/`~" for c in password):
            recomendaciones.append("Añada un símbolo especial (!, @, #, etc.).")
    elif entropia < 80:
        recomendaciones.append("Su contraseña es decente, pero podría ser más segura.")
        if len(password) < 14:
            recomendaciones.append("Considere aumentar la longitud a 14+ caracteres.")
    elif entropia < 100:
        recomendaciones.append("Buena contraseña, pero si puede, use una aún más larga.")
    
    return recomendaciones


#detectar patrones comunes

# Lista de palabras débiles
palabras_comunes = {"password", "admin", "letmein", "welcome", "abc123", "123456", "qwerty", "iloveyou"}
secuencias_teclado = ["qwerty", "asdfgh", "zxcvbn"]

def detectar_repeticiones(password, min_repeticiones=3):
    for i in range(len(password) - min_repeticiones + 1):
        if len(set(password[i:i + min_repeticiones])) == 1:
            return " Contiene caracteres repetidos consecutivos."
    return None

def detectar_secuencias(password, min_secuencia=4):
    for secuencia in secuencias_teclado:
        if secuencia in password.lower():
            return " Contiene una secuencia de teclado predecible."

    for i in range(len(password) - min_secuencia + 1):
        subcadena = password[i:i + min_secuencia]
        if subcadena.isdigit():
            numeros = list(map(int, subcadena))
            if numeros == list(range(numeros[0], numeros[0] + min_secuencia)) or \
               numeros == list(range(numeros[0], numeros[0] - min_secuencia, -1)):
                return " Contiene una secuencia numérica predecible."
    return None

def detectar_palabras_comunes(password):
    if password.lower() in palabras_comunes:
        return " Es una palabra común y fácil de adivinar."
    return None

def detectar_patrones(password):
    alertas = []
    for funcion in [detectar_repeticiones, detectar_secuencias, detectar_palabras_comunes]:
        resultado = funcion(password)
        if resultado:
            alertas.append(resultado)
    return alertas
