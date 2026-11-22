import pyttsx3 
import random
def speak(texto):
    engine = pyttsx3.init()

    engine.setProperty("rate", 150)
    engine.setProperty("volume", 0.9)

    engine.say(texto)

    engine.runAndWait()
speak("Bienvenido al juego de adivinar un numero!")

numero = random.randint(1,10)
puntaje = 0
intentos = 7 

for i in range(1, intentos + 1):
    speak("Cual crees que es el numero!")
    guees = int(input("Cual crees que es el numero:"))

    if numero == guees:
        speak("Felicidades, has adivinado el numero")
        puntaje += 1
        intentos += 7
        numero = random.randint(1,10)
    elif guees < numero:
        speak("El numero que debes adivinar es mayor")
    else:
        speak("El numero que debes adivinar es menor")
speak(f"Gracias por jugar, has obtenido {puntaje} puntos")
