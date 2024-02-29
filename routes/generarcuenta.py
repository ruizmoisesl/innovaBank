import random

def generar_numero_cuenta():
    return f"{random.randint(10**9, 10**10 + 1)}"