import random
import categorias

# ACA PRUEBO MIS FUNCIONES INTEGRANDO EL RANDOM NUEVO DE NOE
# ACA EL PROFE HACE UN COMENTARIO


opcionElegida = ""
dados = []
contadorTiradas = 1


# Esta función es la tirada random de X cantidad de dados
# se la invoca para la primer tirada de 5 dados
# también puede volver a invocarse para volver a tirar los 5 dados
# o para tirar nuevamente una cantidad x de dados elegidos
def tirar_dados(dados):
    for i in range(5):
        dados.append(random.randint(1,6))
    return dados


# Ésta función le explica al usuario cómo proceder,
# pide que elija el procedimiento a seguir y devuelve esa elección
def elegirProcedimiento():
    print("Desea tirar otra vez? Presione V para volver a tirar todos los dados,\nE para elegir qué dados tirar o T para terminar y quedarse con la tirada obtenida.")
    procedElegido = input("Por favor, ingrese su elección: ")
    global opcionElegida
    opcionElegida = procedElegido.upper()
    return procedElegido.upper()


# Ésta función vuelve a tirar los 5 dados nuevamente:
# primero le suma 1 al contador de tiradas,
# después imprime qué número de tirada es y avisa que "va a obtener los siguientes dados"
# luego pide que se borren los valores en la lista de dados
# y por ultimo devuelve la lista de los nuevos dados obtenidos (mediante la invocación de la tirada random)
def tirarTodoNuevo():
    global contadorTiradas
    contadorTiradas = contadorTiradas + 1
    print("La tirada número",contadorTiradas,"obtuvo los siguientes dados:")
    dados.clear()
    return tirar_dados(dados)


# Ésta función simplemente imprime y devuelve la lista de dados con las que
# el usuario eligió quedarse tras haber decidido terminar su turno
# o tras haber agotado las 3 tiradas posibles.
def aceptarTirada():
    print("Turno finalizado. Se ha quedado con los siguientes dados:")
    return dados

def definiciones():
    print("Turno finalizado. Se ha quedado con los siguientes dados:")
    print(dados)
    if dados==categorias.esEscalera(jugada=dados):
        print("obtuvo una escalera",dados)
    if dados==categorias.esFull(jugada=dados):
        print("obtuvo full", dados)
    if dados==categorias.EsGenerala(jugada=dados):
        print("obtuvo generala")
    if dados==categorias.EsPoker(jugada=dados):
        print("obtuvo poker")
    if dados!=categorias.esEscalera(jugada=dados) and dados!=categorias.esFull(jugada=dados) and dados!=categorias.EsGenerala(jugada=dados) and dados!=categorias.EsPoker(jugada=dados):
        valor=int(input("ingrese el valor del cual quiere ver las repeticiones"))
        return categorias.SalidaDeNumero(jugada=dados,valor=valor)


# Ésta función es para elegir uno o varios dados de una lista de dados previa
# para que luego esa cantidad x de dados sea tirada nuevamente y obtenga un nuevo valor.
# Para eso se invoca a la función random sólo para cambiar los valores de los dados elegidos,
# luego se le suma 1 al contador de tiradas,
# se imprime qué número de tirada es y avisa que "va a obtener los siguientes dados"
# y finalmente devuelve el valor de la nueva tirada con los valores de los 5 dados.
def modificarDados():
    dadosAtirar = input("Ingrese los dados a cambiar separados por comas: ")
    lista_dados_cambiados = dadosAtirar.split(",")
    for i in lista_dados_cambiados:
        dados[(int(i))-1]=random.randint(1,6)
    global contadorTiradas
    contadorTiradas = contadorTiradas + 1
    print("La tirada número",contadorTiradas,"obtuvo los siguientes dados:")
    return dados

# Lo que hace esta "lista" (en realidad no es una lista, es un Diccionario)
# Es asignarle a la CLAVE "Opción elegida por el usuario" el VALOR de "El nombre de la función que realiza esa opción"
# Por lo tanto, asocia una con otra.
ref_opciones = {
    "T":aceptarTirada,
    "V":tirarTodoNuevo,
    "E":modificarDados
}


# ESTE SERÍA EL PROGRAMA PRINCIPAL
# Primero imprime el numero de tirada
# Luego invoca la función de tirar los dados random (por defecto 5 dados) para luego mostrar los dados
# Después entra en un while donde se deben cumplir AMBAS condiciones
# la primer condición es que el contador de tiradas sea distinto a 3
# la segunda es que la opción del procedimiento elegido debe ser distinto a T (terminar)
# Si ambas se cumplen se invoca a la opción elegida en la función "elegirProcedimiento"
# imprimiendo la CLAVE y el VALOR de la opción elegida usando la Lista(diccionario)
# imprimiendo la CLAVE y el VALOR de la opción elegida usando la Lista(diccionario)
# Dentro del While hay un For: Donde, si el usuario escribió un caracter correcto y
# el resultado de la condicion es true, realiza la función a la que está asociada el caracter.
# Si el caracter ingresado es incorrecto, imprime un mensaje de error,
# avisando que el usuario se equivocó y pidiendo que ingrese otro caracter.
# Se vuelve a entrar en el ciclo while indefinidamente.
# Finalmente si la opción elegida es T o se cumplen las 3 tiradas
# finaliza el ciclo while e invoca la función aceptar tirada
# para imprimir la tirada final con la que el usuario se quedó.

def programa_principal():
    print("La tirada número",contadorTiradas,"obtuvo los siguientes dados:")
    tirar_dados(dados)
    print(dados)
    while contadorTiradas != 3 and elegirProcedimiento() != "T":
        if opcionElegida in ref_opciones:
         print(ref_opciones[opcionElegida]())
        else:
            print("ERROR. Esa opción no es correcta. Por favor ingrese una opción válida.")
    return definiciones()

# ACÁ TERMINA EL PROGRAMA

# Ya corregí lo que me faltaba, ahora ingresando cualquier caracter incorrecto
# salta un mensaje de error y vuelve a ingresar en el ciclo while.