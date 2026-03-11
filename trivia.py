usuario = input("ingrese su nombre")
print(f"Bienvenid@ {usuario}a esta trivia")


# Pregunta 1
respuesta = input("¿Capital de Francia? ")
if respuesta.lower() == "paris":
    puntaje += 1

# Pregunta 2
respuesta = input("¿Cuánto es 5 + 3? ")
if respuesta == "8":
    puntaje += 1

# Pregunta 3
respuesta = input("¿Color del cielo en un día despejado? ")
if respuesta.lower() == "azul":
    puntaje += 1

# Pregunta 4
respuesta = input("¿Animal que dice miau? ")
if respuesta.lower() == "gato":
    puntaje += 1

print("Jugador:", nombre)
print("Puntaje final:", puntaje)

if puntaje == 4:
    print("Excelente")
elif puntaje >= 2:
    print("Muy bien")
else:
    print("Puedes mejorar")