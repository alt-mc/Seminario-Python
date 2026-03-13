import random

words = [
    "python",
    "programa",
    "variable",
    "funcion",
    "bucle",
    "cadena",
    "entero",
    "lista",
]
word = random.choice(words)
guessed = []
attempts = 6

# INICIO MODIFICACOIN 2
puntos = 0
# FIN MODIFICACION 2

print("¡Bienvenido al Ahorcado!")
print()
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")

        # INICIO MODIFICACION 2
        puntos += 6
        # FIN MODIFICACION 2

        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ").lower()

    # INICIO MODIFICACION 1
    if len(letter) != 1 or not letter.isalpha():
        print("Entrada no valida!!")
        continue
    # FIN MODIFICACION 1

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1

        # INICIO MODIFICACION 2
        puntos -= 1
        # FIN MODIFICACION 2

        print("Esa letra no está en la palabra.")
    print()
else:
    print(f"¡Perdiste! La palabra era: {word}")
    # INICIO MODIFICACION 2
    puntos = 0
    # FIN MODIFICACION 2

# INICIO MODIFICACION 2
print(f"Puntaje final: {puntos}")
# FIN MODIFICACION 2
