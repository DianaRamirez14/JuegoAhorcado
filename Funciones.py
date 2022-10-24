
"""
Requerimientos 
1. La palabra adivinar se debe seleccionar aleatoriamente del listado disponible en un archivo de texto

2. El jugador tendrá 5 turnos para adivinar la palabra (independientemente si en cada jugada tiene un acierto o un fallo)

3. En cada turno tenemos lo siguiente:
- Se debe mostrar al usuario la actualizacion de la palabra que se está intentado adivinar y el alfabeto tambien se debe actualizar (es decir, las letras que se encuentren disponibles)

- Se debe preguntar al usuario si desea adivinar la palabra, y de ser asi realizar la verificacion correspondiente
4. El juego termina:

- Se completan los 5 turnos y el jugador no acierta
- El jugador decide adivinar la palabra y acierta
"""

import random


# Funcion para escoger un palabra random
def seleccionarPalabra():
  lineas = open("frutas_verduras.txt").readlines()
  palabra = random.choice(lineas).rstrip()
  return palabra

# Funcion entrada de teclado
def entradaUsuario():
  letra = input("Introduzca una letra: ")
  return letra.lower()

# Funcion actualizar jugada
def actualizarJugada(palabra, letra, jugada):
  n_letras = len(palabra)

  for i in range(0, n_letras):
    if palabra[i] == letra:
      jugada[i] = letra
      
  return jugada
# Actualizar alafabeto
def actualizarAlfabeto(letra, alfabeto):
  alfabeto = alfabeto.replace(letra, " ")
  return alfabeto
# Imprimir resultado de la jugada en pantalla
def imprimirActualizacion(alfabeto, jugada):
  print (f"Jugada: {jugada}")
  print (f"Letras disponibles: {alfabeto}")
  
#Verificar jugada
def verificarJugada(suposicion, palabra):
  success = False
  if suposicion == palabra:
    success = True
  return success


