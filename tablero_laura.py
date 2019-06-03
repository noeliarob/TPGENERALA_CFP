from tabulate import tabulate

def ingresoCantidadJug ():#Esta función es para obtener y retornar la cantidad de jugadores ingresada por el usuario.
    cantidad = int(input("Por favor, ingrese la cantidad de jugadores: "))
    return cantidad

def ingresoNombres (cantidad):#Esta función sirva para agregar los nombres de los jugadores a la lista Vacía de jugadores
    for cantidad in range(0, cantidad):
        jugadores.append(input("Por favor ingrese nombre del jugador: "))

def insertarColumnas (cantidad):#Sirve para agregar X cantidad de "espacios" agregando un 0 por cada jugador en cada "Vagón" de la lista puntajeParcial
    for t in range (0,cantidad):#Por ejemplo si ponemos 3 en cantidad se va a agregar 1 cero por iteración en los 12 vagones (de 1-6, E,F,P,G,GD y el espacio del resultado final)
        for posiciones in range (0,12):#Estos son los doce "vagones"
            puntajeParcial[posiciones].append(0)#acá agrega el valor 0 en el vagón X(cambia según la iteración)

def sumaPuntajeFinal(cantidad,puntajeParcial):# Se debe agregar esta función solo al final, porque si los valores están vacíos no se pueden sumar
    for nume in range(1, cantidad+1):# Debe estar completo el ingreso de los 11 valores por jugador, lo que no tenga completo se debe agregar 0
        resultado = ((puntajeParcial[0][nume])+(puntajeParcial[1][nume])+(puntajeParcial[2][nume])+
                     (puntajeParcial[3][nume])+(puntajeParcial[4][nume])+(puntajeParcial[5][nume])+
                     (puntajeParcial[6][nume])+(puntajeParcial[7][nume])+(puntajeParcial[8][nume])+
                     (puntajeParcial[9][nume])+(puntajeParcial[10][nume]))
        puntajeParcial[11][nume] = (resultado)
    cadenaPuntaje =(" PUNTAJE FINAL ")
    print("\n"+(cadenaPuntaje.center(50,"=")+"\n"))
    mostrarPuntajeParcial()

########## ACA ESTOY MODIFICANDO ESTO DE LA ANTERIOR #######

def anotacion (nroJugador):#Esto es para ingresar los puntos, hay que cambiar las opciones a un diccionario para validar si hay un error de tipeo.
    categoria = input("Ingrese categoria a anotar (Ingresando 1, 2, 3, 4, 5, 6, E, F, P, G, GD): ")
    puntos = int(input("Ingrese cantidad de puntos obtenidos: "))
    if categoria == '1':
        puntajeParcial[0][nroJugador] = puntos
    elif categoria == '2':
        puntajeParcial[1][nroJugador] = puntos
    elif categoria == '3':
        puntajeParcial[2][nroJugador] = puntos
    elif categoria == '4':
        puntajeParcial[3][nroJugador] = puntos
    elif categoria == '5':
        puntajeParcial[4][nroJugador] = puntos
    elif categoria == '6':
        puntajeParcial[5][nroJugador] = puntos
    elif categoria.upper() == 'E':
        puntajeParcial[6][nroJugador] = puntos
    elif categoria.upper() == 'F':
        puntajeParcial[7][nroJugador] = puntos
    elif categoria.upper() == 'P':
        puntajeParcial[8][nroJugador] = puntos
    elif categoria.upper() == 'G':
        puntajeParcial[9][nroJugador] = puntos
    elif categoria.upper() == 'GD':
        puntajeParcial[10][nroJugador] = puntos

def mostrarPuntajeParcial():#Esto muestra el tablero con los resultados parciales
    print(tabulate(puntajeParcial, jugadores))

def mostrarGanador (puntajeParcial,cantidad,jugadores):#Muestra que jugador ganó y con cuantos púntos
    puntajeMaximo = (max(puntajeParcial[11][1:]))
    for posicion in range(0,cantidad):
        if puntajeMaximo == (puntajeParcial[11][posicion+1]):
            print("\nEl ganador del juego es " + (str(jugadores[posicion])) + " con " + (str(puntajeMaximo)) + " puntos.")

# ACÁ COMIENZA EL PROGRAMA PRINCIPAL, HAY QUE PONER PRIMERO LO DE "FROM TABULATE IMPORT TABULATE" QUE DEJÉ PUESTO AL INICIO

jugadores = []
puntajeParcial = [['1'],['2'],['3'],['4'],['5'],['6'],['E'],['F'],['P'],['G'],['GD'],['']]
cantidad = 0

cantidad = ingresoCantidadJug()
ingresoNombres(cantidad)
insertarColumnas(cantidad)

#for turno in range(0,2):#El 2 hay que cambiarlo por 11, que es la cantidad de turnos por jugador. Puse 2 para no probar los 11 turnos.
 #   print("\n* Turno número", str(turno + 1)+" *\n")
  #  for a in range(0,cantidad):
   #     print("Debe tirar el jugador Número",(a + 1),":",(jugadores[a]))#Entre esta función y la siguiente hay que agregar la tirada random y lo de jugadas especiales.
    #    anotacion(a+1)#Una vez que tenemos la jugada final y la detección de jugada especial se invoca a esta función para anotar.
     #   # Hay que cambiarle la función donde el usuario ingresa los valores por una función que los agregue automaticamente al detectarlos.
      #  # O en su defecto, hay que agregar una función que valide si los datos ingresados son correctos.
       # print("")
    #print("* Resultados Parciales *\n")
    #mostrarPuntajeParcial()# Luego de ingresar cada anotación se muestran los resultados parciales.

#sumaPuntajeFinal(cantidad,puntajeParcial) #Esto solo se pone al final sino va a saltar error.
#mostrarGanador(puntajeParcial,cantidad,jugadores) # Muestra que jugador ganó y con cuántos puntos
