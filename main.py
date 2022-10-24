from Funciones import *

#Seleccionar palabra e inicializar el alfabeto y jugada
def main(): #Para definir una función
  palabra = seleccionarPalabra()
  alfabeto = "a b c d e f g h i j k l m n ñ o p q r s t u v w x y z"
  jugada = ['_'] * len (palabra)
  for turno in range(5):
    print (f"\nTurno:{turno+1}")
    print("-"*20)
    #Imprimir alfabeto y jugada
    imprimirActualizacion(alfabeto, jugada)
    #Entrada usuario
    letra = entradaUsuario()
     #Actualizar jugada y alfabeto
    jugada = actualizarJugada(palabra, letra, jugada)
    alfabeto = actualizarAlfabeto(letra, alfabeto)
    #Imprimir actualizacion
    imprimirActualizacion(alfabeto, jugada)
    #Preguntar al usuario si desea adivinar ó no la palabra
    check = input("¡Desea adiviar la palabra? (si/no):")
    if check.lower() == "si":
      suposicion = input ("Introduzca su respuesta: ").lower()
      success = verificarJugada(suposicion, palabra)
    #
      if success:
        print("+"*20)
        print("GANÓ")
        print("+"*20)
        break
      else:
        print("+"*20)
        print("La suposición es incorrecta :C")
        print("+"*20)
        
    if turno == 4:
      print("-"*20)
      print(":c :c AHORCADOOO, NOOO")
      print("-"*20)

if __name__=="__main__":
  main ()