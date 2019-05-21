def EsGenerala(jugada):
   for i in jugada:
      if jugada.count(jugada[i])==5:
          return True
      else:
          return False
