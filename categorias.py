def SalidaDeNumero(jugada,valor):
  cantidad_de_repeticiones=0
  for i in jugada:
      if i==valor:
          cantidad_de_repeticiones+=1
  return print("El dado",valor,"salio:",cantidad_de_repeticiones,"veces")

def EsGenerala(jugada):
   for i in jugada:
      if jugada.count(jugada[i])==5:
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

def esFull(jugada):
    contador=0
    for i in jugada:
        if jugada.count(jugada[i])==3:
            contador=+1
        elif jugada.coun(jugada[i])==2:
            contador=+1
        elif contador==2:
            return True
        else:
            return False