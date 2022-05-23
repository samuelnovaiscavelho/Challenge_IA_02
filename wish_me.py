from datetime import datetime
from speak import speak

def wish_me(name):
    hour = int(datetime.now().hour)

    if 0 <= hour < 12:
        speak(f"Olá, bom dia! Seja bem vindo ao processo seletivo {name}.")

    elif 12 <= hour < 18:
        speak(f"Olá, boa tarde! Seja bem vindo ao processo seletivo {name}.")

    else:
        speak(f"Olá, boa noite! Seja bem vindo ao processo seletivo {name}.")