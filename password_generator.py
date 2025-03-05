# password_generator.py
import random
import string
import hashlib


def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    caracteres = ''.join(c for c in caracteres)

    return ''.join(random.choice(caracteres) for _ in range(longitud))


def generar_contraseña_moviles(longitud=12):
    caracteres = string.ascii_lowercase + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))


def generar_contraseña_hash(frase):
    hash_md5 = hashlib.sha256(frase.encode()).hexdigest()
    return hash_md5[:]


from password_analyzer import calcular_entropia

def generar_contraseña_segura(longitud=12, intentos=10):
    for _ in range(intentos):
        password = generar_contraseña(longitud)
        if calcular_entropia(password) > 60:
            return password
        
def generar_contraseña_personalizada(longitud=12, incluir_mayus=True, incluir_minus=True, incluir_numeros=True, incluir_simbolos=True, excluir=""):
    caracteres = ""
    if incluir_mayus:
        caracteres += string.ascii_uppercase
    if incluir_minus:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    # Excluir caracteres específicos
    caracteres = ''.join(c for c in caracteres if c not in excluir)

    if not caracteres:
        raise ValueError("No hay suficientes caracteres disponibles para generar la contraseña.")
    
    # Asegurar que sea segura
    for _ in range(10):  # Intenta hasta 10 veces generar una contraseña segura
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        if calcular_entropia(contraseña) > 60:
            return contraseña

    return None
