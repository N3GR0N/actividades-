import random

# Lista de palabras posibles
words = ["python", "programación", "computadora", "código", "desarrollo", "inteligencia"]

# Elegir una palabra al azar
secret_word = random.choice(words)

# Número máximo de errores permitidos decido que sera 5 
max_errors = 5

# Lista para almacenar las letras adivinadas
guessed_letters = []

print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "_" * len(secret_word)

# Mostrar la palabra parcialmente adivinada
print(f"Palabra: {word_displayed}")

#numero de errores actuales que usaremos como contador 
errors = 0 

while errors < max_errors:
    # Pedir al jugador que ingrese una letra
    letter = input("Ingresa una letra: ").lower()

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print("Ya has intentado con esa letra. Intenta con otra.")
        continue

    # Verificar si la letra está vacía
    if letter == "":
        print("ERROR!!, la letra ingresada es inválida, por favor ingrese otra.")
    else:
        # Agregar la letra a la lista de letras adivinadas
        guessed_letters.append(letter)

        # Verificar si la letra está en la palabra secreta y contar errores si la letra no está en la palabra
        if letter in secret_word:
             print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Lo siento, la letra no está en la palabra.")
            errors = errors +  1

    # Mostrar la palabra parcialmente adivinada
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f"Palabra: {word_displayed}")
    
    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
        break
else:
    print(f"Lo siento, Has cometido {max_errors} errores y lamentablemente has perdido.")
    print(f"La palabra secreta era: {secret_word}")
    