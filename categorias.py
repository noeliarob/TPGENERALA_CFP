#c:Python>python -m pip install -- upgrade pip (actualiaar) para instalar paquetes tengo que instalar pip, tabulate 42 lo debo
from collections import Counter

#me pide un valor, y recorre cuantas veces esta ese valor dentro de la jugada
def SalidaDeNumero(jugada,valor):
  cantidad_de_repeticiones=0
  for i in jugada:
      if i==valor:
          cantidad_de_repeticiones+=1
  return print("El dado",valor,"salio:",cantidad_de_repeticiones,"veces")

#la i toma el primer valor de jugada hasta el ultimo, y pregunta valor por valor la caantidad de veces que esta.
#si el valor i esta 5 veces dentro de jugada, me retorna true
def EsGenerala(jugada):
   for i in range (0,len(jugada)):
      if jugada.count(jugada[i])==5:
          return True
      else:
          return False

#la i toma el primer valor de jugada hasta el ultimo, y pregunta valor por valor la caantidad de veces que esta.
#si el valor i esta 4 veces dentro de jugada, me retorna true
def EsPoker(jugada):
   for i in range (0,len(jugada)):
      if jugada.count(jugada[i])==4:
          return True
      else:
          return False

#la i toma el primer valor de jugada hasta el ultimo, y pregunta valor por valor la caantidad de veces que esta.
#si el valor i esta 3 veces dentro de jugada, me retorna true
#si hay otro valor que esta 2 veces me retorna true.
def esFull(jugada):
    hay_tres=False
    hay_dos=False
    for i in range (0,len(jugada)):
        if jugada.count(jugada[i])==3:
            hay_tres=True
        if jugada.count(jugada[i])==2:
           hay_dos=True
    return hay_tres and hay_dos

#la funcion establece las dos posibles escaleras que existen dentro del juego.
#luego ordena la jugada, si es igual a alguna de las dos escaleras retorna true.
def esEscalera(jugada):
    esc1=[1,2,3,4,5]
    esc2=[2,3,4,5,6]
    if sorted(jugada)==esc1 or sorted(jugada)==esc2:
        return True
    else:
        return False
