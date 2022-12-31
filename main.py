import random


# Función que muestra las opciones del juego
def mostrar_opciones():
  print("1. Piedra")
  print("2. Papel")
  print("3. Tijera")


# Función que recibe la opción del usuario y la opción de la computadora
# y determina quién gana
def determinar_ganador(opcion_usuario, opcion_computadora):
  if opcion_usuario == opcion_computadora:
    print("Empate")
  elif opcion_usuario == 1 and opcion_computadora == 3:
    print("Ganaste")
  elif opcion_usuario == 2 and opcion_computadora == 1:
    print("Ganaste")
  elif opcion_usuario == 3 and opcion_computadora == 2:
    print("Ganaste")
  else:
    print("Perdiste")


# Bucle principal del juego
print('*' * 35)
print('JUEGO DE PIEDRA, PAPEL Y TIJERA')
print('*' * 35)

while True:
  print('')
  print("Elige una opción:")
  mostrar_opciones()
  opcion_usuario = int(input())

  #Validar resultado
  if not opcion_usuario in [1,2,3]:
    print('Opcion invalida ¡VUELVE A INGRESAR¡')
    continue

  # Generar una opción aleatoria para la computadora
  opcion_computadora = random.randint(1, 3)

  if opcion_computadora == 1:
    print("La computadora eligió: Piedra")
  elif opcion_computadora == 2:
    print("La computadora eligió: Papel")
  else:
    print("La computadora eligió: Tijera")

  # Determinar quién gana
  print('')
  determinar_ganador(opcion_usuario, opcion_computadora)

  # Preguntar al usuario si quiere volver a jugar
  print('')
  print("¿Quieres jugar de nuevo? (s/n)")
  jugar_de_nuevo = input()
  if jugar_de_nuevo.lower() != "s":
    break
