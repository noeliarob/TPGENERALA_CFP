#si no esta, agregar tabulate, boton rojito por encima del from, instale package. Me lo instala solo.
from tabulate import tabulate

#inicializar dos listas:
nombres=[]
#puntos, establecer en el ablero cuantos puntos tuvo cada jugador. Se puede hacer un diccionario para esto, o establecer una variable asi:
tanteador=["1","2","3","4","5","6","E","F","P","G","DG"]
puntos=[]

#tablero de os jugadores establecer que son 11 por jugador, por que tienen 11 tiradas cada uno. Cada jugador va a tener un tablero todo el 0.
#se corresponde la posicion de tablero con el tanteador.
tablero=[0,0,0,0,0,0,0,0,0,0,0]
#ingresar la cantidad de jugadores
cant=int(input("ingrese canidad de jugadores:"))

for i in range(0,cant):
   nombres.append(input("ingrese nombre"))
   puntos.append(tablero)

#print(nombres)
#print(puntos)
#asterisco significa parametros no definidos.
#map crea un mapa de la lista.
listado=list(map(list,zip(*puntos)))
print(tabulate(listado,showindex=tanteador,headers=nombres,tablefmt="presto"))


