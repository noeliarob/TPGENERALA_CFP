#c:Python>python -m pip install -- upgrade pip (actualiaar) para instalar paquetes tengo que instalar pip, tabulate 42 lo debo
from collections import Counter

def SalidaDeNumero(jugada,valor):
  cantidad_de_repeticiones=0
  for i in jugada:
      if i==valor:
          cantidad_de_repeticiones+=1
  return print("El dado",valor,"salio:",cantidad_de_repeticiones,"veces")

def EsGenerala(jugada):
   for i in jugada:
      if jugada.count(jugada[i])==5:
          print((jugada[i]))
          return True
      else:
          return False

def EsPoker(jugada):
   for i in jugada:
      if jugada.count(jugada[i])==4:
          return True
      else:
          return False

def EsFull(jugada):
   contador = len(Counter(jugada))
   if contador==2:
       return True
   else:
       return False

#def esFull(jugada):
 #   contador=0
  #  for i in jugada:
   #     if jugada.count(jugada[i])==3:
    #        contador=+1
     #       if jugada.count(jugada[i])==2:
      #      contador=+1
       # if contador==2:
        #        return True
        #else:
        #    return False

#def esFull(jugada):
 #   for i in jugada:
  #      if int(jugada.count(jugada[i]))==3 and int(jugada.count(jugada[i]))==2:
   #         return True
    #    else:
     #       return False

def ordenarDados(jugada):
    ordenar=sorted(jugada)
    return ordenar

def esEscalera(jugada):
    esc1=[1,2,3,4,5]
    esc2=[2,3,4,5,6]
    if jugada==esc1 or jugada==esc2:
        return True
    else:
        return False
