# base_datos
#algunas funciones de base de datos
import tablero_laura
import sqlite3
from datetime import datetime
base=sqlite3.connect('C://Noelia_base//base_datos.db')
c=base.cursor()

###FUNCION QUE ME PERMITE GUARDAR LOS NOMBRES DE LOS JUGADORES EN LA TABLA JUGADORES CUANDO SE INGRESAN###
###LLAMA A LA VARIABLE JUGADORES, LISTA QUE SE OBTIENE DE LA FUNCION DE AGREGAR LA CANTIDAD DE JUGADORES##
###SEGUIDA POR LOS NOMBRES###
def guardar_jugadores(jugadores):
    for i in jugadores:
        c.execute('insert into JUGADORES (NOMBRES) values ("{}");'.format(i))
    base.commit()

###FUNCION QUE GUARDA EL NOMBRE DE LA PARTIDA EN LA TABLA DE PARTIDAS, JUNTO CON SU FECHA Y HORA AL MOMENTO DE INGRESARLA###
def guardar_partida(nombre_partida):
    fecha = datetime.now()
    c.execute('insert into PARTIDA (NOMBRE_PARTIDA,FECHA_HORA) values ("{}","{}");'.format(nombre_partida,fecha))
    base.commit()

###UNIR TODAS LAS DE RESULTADOS PARCIALES EN UNA SOLA FUNCION:
###TENGO QUE UTILIZAR LA ULTIMA LISTA DE DADOS CON LA QUE SE QUEDO EL JUGADOR.
def guardar_dados(dados): ####los dados definitivos estan en la funcion: aceptartirada
    c.execute('insert into RESULTADOS_PARCIALES_USUARIOS(d1,d2,d3,d4,d5) values ({},{},{},{},{});'.format(dados[0],dados[1],dados[2],dados[3],dados[4]))
    base.commit()

######UNIR TODAS LAS DE RESULTADOS PARCIALES EN UNA SOLA FUNCION:
###NECESITO QUE UNA VEZ QUE EL JUGADOR TIRÓ Y SE QUEDO CON LOS DADOS: ME QUEDE EN UNA LISTA LA CANTIDAD DE PUNTAJE QUE OBTUVO
###EN ESA JUGADA: EJEMPLO:
###1 2 3 4 5 6 E F P G 2G
##[0,0,0,8,0,0,0,0,0,0,0]

####VA A LLEGAR UNA LISTA QUE CONTIENE:
####["1",0,0,0]#  - "1": ES LA CATEGORIA, PUEDE FER "E","G",ETC. ... LA CANTIDAD DE 0 ES LA CANTIDAD DE JUGADORES QUE HAY,

##
def guardar_resultados(resultados_parciales):
    c.execute('insert into RESULTADOS_PARCIALES_USUARIOS("1","2","3","4","5","6",E,F,P,G,"2G") values ({},{},{},{},{},{},{},{},{},{},{});'.format(resultados_parciales[0],resultados_parciales[1],resultados_parciales[2],resultados_parciales[3],resultados_parciales[4],resultados_parciales[5],resultados_parciales[6],resultados_parciales[7],resultados_parciales[8],resultados_parciales[9],resultados_parciales[10]))
    base.commit()

####UNIR TODAS LAS DE RESULTADOS PARCIALES EN UNA SOLA FUNCION:
####GUARDAR LA CANTIDAD DE TIRADAS QUE SE OBTUVO AL APRETAR T: QUE ES CUANDO SE QUEDA CON LA PARTIDA OBTENIDA.
def guardar_lanzadas(contadorTiradas): ###supongo que la funcion que recibo es la de contador_tiradas
    c.execute('insert into RESULTADOS_PARCIALES_USUARIOS("LANZADAS") values ({});'.format(contadorTiradas))
    base.commit()

####UNIR TODAS LAS DE RESULTADOR PARCIALES EN UNA SOLA FUNCION:
###GUARDA EL ID DE PARTIDA EN LA TABLA DE RESULTADOS_PARCIALES


def guardar_idPartida():
    id_partida='insert into RESULTADOS_PARCIALES_USUARIOS("ID_PARTIDA") values (SELECT ID FROM PARTIDA WHERE NOMBRE_PARTIDA="{}"))'.format(nombre_partida)
    c.execute(id_partida)
    base.commit()

def guardar_idJugadores():
    id_jugadores='insert into RESULTADOS_PARCIALES_USUARIOS("ID_JUGADORES") values (SELECT * ID FROM JUGADORES WHERE NOMBRES="{}"))'.format(jugadores)
    c.execute(id_jugadores)
    base.commit()


def guardar_result_parciales(id_partida,id_jugadores,resultados_parciales,dados,contadorTiradas):
    c.execute('insert into ')

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


######CUANDO HAGO UN SELECT UTILIZO fetchal######
######c.execute('select * from JUGADORES')#######
######r = c.fetchall()###########################
######print(r)###################################

#####################################################
###ACA ESTOY SIMULANDO LA LLAMADA DE LAS FUNCIONES###
#####################################################
jugadores=tablero_laura.jugadores
guardar_jugadores(jugadores)

nombre_partida=input("ingrese nombre de la partida")
guardar_partida(nombre_partida)

resultados_parciales=[0,0,0,12,0,0,0,0,0,0,0]
guardar_resultados(resultados_parciales)

dados=[1,2,3,4,5]
guardar_dados(dados)


contadorTiradas = 2
guardar_lanzadas(contadorTiradas)

#id_jugadores='SELECT ID FROM JUGADORES WHERE JUGADORES.NOMBRES={});'.format(jugadores)
#guardar_idJugadores()

#id_partida='SELECT ID FROM JUGADORES WHERE PARTIDA.NOMBRE_PARTIDA={});'.format(nombre_partida)
guardar_idPartida()


##### esto es si no existe una partida con ese nombre la cree.
#####existe=existe_partida(nombre_partida)
#####if not existe:
#####  guardar_partida(nombre_partida)
#####else:
#####   print(existe)