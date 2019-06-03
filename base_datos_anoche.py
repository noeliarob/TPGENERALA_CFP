# base_datos
#algunas funciones de base de datos
import tablero_laura
import sqlite3
from datetime import datetime
base=sqlite3.connect('C://Noelia_base//base_datos.db')
c=base.cursor()

def guardar_jugadores(jugadores):
    for i in jugadores:
        c.execute('insert into JUGADORES (NOMBRES) values ("{}");'.format(i))
    base.commit()

def guardar_partida(nombre_partida):
    fecha = datetime.now()
    c.execute('insert into PARTIDA (NOMBRES,FECHA_HORA) values ("{}","{}");'.format(nombre_partida,fecha))
    base.commit()

###consultar primero el id de la partida segun el nombre
def guardar_resultados(id_partida,id_jugador,resultados_parciales,dados,lanzada):
    c.execute('insert into RESULTADOS_PARCIALES_USUARIOS(ID_PARTIDA,ID_JUGADOR,1,2,3,4,5,6,E,F,P,G,2G,D1,D2,D3,D4,D5,LANZADAS) values ({},{},{},);'.format(nombre_partida,fecha))

####AGREGAR UNA FUNCION QUE ME VALIDE SI EXISTE UNA PARTIDA:
#esta funcion la voy a usar al momento de crear la partida:
#si me devuelve distinto de falso es que existe la partida y me devuelve el id de la partida, si no devuelve false.
#cuando ingreso un nombre de partida, valido si ya existe una con ese nombre. Esta funcion deberia usarla para no crear dos partidas
#con el mismo nombre.



def existe_partida(nombre_partida):
    query='SELECT ID FROM PARTIDA WHERE NOMBRE="{}" LIMIT 1'.format(nombre_partida)
    c.execute(query)
    partida=c.fetchall()
    if not partida:
        return False
    else:
        return partida[0][0]


######CUANDO HAGO UN SELECT UTILIZO fetchall
#c.execute('select * from JUGADORES')
#r = c.fetchall()
#print(r)

#### Aca estoy simulando llamadas a las funciones
jugadores=tablero_laura.jugadores
guardar_jugadores(jugadores)

nombre_partida=input("ingrese nombre de la partida")
guardar_partida(nombre_partida)


##### esto es si no existe una partida con ese nombre la cree.
##existe=existe_partida(nombre_partida)
##if not existe:
  #  guardar_partida(nombre_partida)
#else:
 #   print(existe)
