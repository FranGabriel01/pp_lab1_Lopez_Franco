import json
import re
import os

def clearconsole() -> None:
    """
    Esta función borra la pantalla de la consola en Python esperando la entrada del usuario y luego
    llamando al comando 'cls' para borrar la pantalla.
    """
    _= input('Presione enter para continuar...')
    os.system('cls')

def leer_json(ruta:str):
    """
    Esta función lee un archivo json y devuelve un diccionario.
    """
    with open(ruta, "r", encoding="utf=8") as archivo:
        contenedor = archivo.read()
        lista_jugadores = json.loads(contenedor)
        return lista_jugadores["jugadores"]
    

lista_jugadores = leer_json(r"C:\Users\Juli\Desktop\Programacion 1\Parcial\dt.json")

#1
def mostrar_jugador(lista:list,dato:str):
    '''
    Recibe una lista y un dato
    Devuelve el jugador encontrado en la lista
    '''

    lista_jugadores = []
    indice = 0
    for indice_jugador in lista:
        lista_jugadores.append("{0} - {1} - {2}".format(indice,indice_jugador[dato],indice_jugador["posicion"]))
        indice += 1
    return "\n".join(lista_jugadores)

#2
def obtener_informacion_jugador(lista: list) -> list:
    """
    Esta función muestra información de un jugador seleccionado por su índice.
    Recibe: Lista_jugadores: Una lista que contiene los jugadores y sus estadísticas.
    Retorna: Lista
    """
    nombre_estadistica = ""  # Inicializar la variable antes del bucle

    indice_jugadores = {}
    # Crear el diccionario indice_jugadores con los nombres completos y estadísticas de los jugadores
    for i in range(len(lista)):
        jugador = lista[i]
        nombre = jugador["nombre"]
        indice_jugadores[i] = {"nombre": nombre, "estadisticas": jugador["estadisticas"]}

    indice_ingresado = None
    while indice_ingresado is None:
        entrada = input("Ingrese un índice entre 0 y 11: ")
        if entrada.isdigit():
            indice_ingresado = int(entrada)
            nombre_estadistica = obtener_nombre_estadisticas(lista, indice_ingresado)
            if indice_ingresado < 0 or indice_ingresado > 11:
                print("Índice inválido, intente nuevamente.")
                indice_ingresado = None
        else:
            print("Entrada inválida, intente nuevamente.")
            indice_ingresado = None

    return nombre_estadistica

    
#3
def obtener_nombre_estadisticas(lista_jugadores: list[dict], indice)-> str:
    """
    Esta función toma una lista de diccionarios que contienen información del jugador y un índice, y
    devuelve una cadena con el nombre del jugador y sus estadísticas separados por comas.
    retorna una cadena que contiene el nombre de un jugador y sus estadísticas, separados por comas. Si
    la lista de entrada está vacía, se devuelve una cadena vacía.
    """
    datos = ""
    if lista_jugadores:
        jugador_indice_ingresado = lista_jugadores[indice]
        jugador_estadisticas = jugador_indice_ingresado["estadisticas"]
        nombre_posicion = "{0}, {1}".format(jugador_indice_ingresado["nombre"], \
                                            jugador_indice_ingresado["posicion"])
        lista_claves = ["nombre", "posicion"]
        lista_valores = []
        print("{0}".format(nombre_posicion))
        for clave in jugador_estadisticas:
            # Imprimir cada estadística
            valor = jugador_estadisticas[clave]
            print("{0} : {1}".format(clave, valor))
            # Agregar la clave a la lista de claves
            lista_claves.append(clave)
            # Agregar el valor (convertido a cadena) a la lista de valores
            lista_valores.append(str(valor))

        claves_str = ",".join(lista_claves)
        valores_str = ",".join(lista_valores)

        datos = "{0}\n{1},{2}".format(claves_str ,nombre_posicion ,valores_str) 

    return datos

def guardar_csv(ruta:str,contenido):
    with open(ruta, "w") as archivo:
       byte = archivo.write(contenido)
       if byte > 0:
           print("Se creo el archivo")
       else:
           print("No se creo el archivo")

#4
def buscar_jugador_por_nombre(lista:list) -> list:
    flag = True
    lista_jugadores = []
    nombre_ingresado = input("Ingrese el nomrbre de un jugador: ")
    nombre_ingresado = nombre_ingresado.capitalize()
    if re.search('[a-zA-Z ]+',nombre_ingresado):
        for jugador in lista:
            if nombre_ingresado in jugador["nombre"]:
                flag = False
                lista_jugadores.append(jugador)
        if flag:
            print("No se encontro ningun jugador con ese nombre")
    return lista_jugadores
    
def imprimir_dato(lista:list,dato:str):
    for jugador in lista:
        print("\n",jugador["nombre"])
        for logro in jugador[dato]:
            print(logro)

#5
def calcular_promedio(lista:list,dato:str):
    '''
    Recibe una lista y un dato especifico
    Calcula el promedio de un dato en especifico
    retorna promedio con 2 decimales
    '''

    jugadores = len(lista)
    promedio = 0
    if len(lista) == 0:
        return -1
    for jugador in lista:
        promedio = promedio + jugador["estadisticas"][dato]
    promedio = promedio / jugadores
    return round(promedio,2)

def ordenar_palabra(lista:list,dato:str) -> list:
    '''
    Recibe una lista y un dato especifico
    ordena lista en forma ascendente
    retorna una lista ordenada
    '''

    lista_izq = []
    lista_der = []
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        for elemento in lista[1:]:
            if (elemento[dato] > pivot[dato]):
                lista_der.append(elemento)
            else:
                lista_izq.append(elemento)
                    
    lista_izq = ordenar_palabra(lista_izq,dato)
    lista_izq.append(pivot)
    lista_der = ordenar_palabra(lista_der,dato)
    lista_izq.extend(lista_der)
    return lista_izq

def formato_cadena(lista:list,dato1:str,dato2:str):
    '''
    Recibe una lista y dos datos especificos
    formatea cadena en forma ascendente
    retorna cadena ordenada
    '''
    for jugador in lista:
        nombre_jugador = jugador[dato1]
        jugador_puntaje = jugador["estadisticas"][dato2]
        print("{0} - {1}".format(nombre_jugador,jugador_puntaje))

#7
def calcular_mayor(lista: list, dato: str) -> list[str]:
    """
    Esta función recorre una lista de jugadores y encuentra jugadores que tienen el mayor valor en una estadística específica.
    Recibe por parámetros una lista y un dato específico.
    Retorna una lista de cadenas con los jugadores y los valores correspondientes.
    """
    mayor = 0  
    lista_mayor = []

    for jugador in lista:
        estadisticas = jugador["estadisticas"]
        if dato in estadisticas:
            valor_estadistica = estadisticas[dato]
            if valor_estadistica > mayor:
                mayor = valor_estadistica
                lista_mayor = ["{0}: {1}".format(jugador["nombre"],mayor)]
            elif valor_estadistica == mayor:
                lista_mayor.append("{0}: {1}".format(jugador["nombre"],mayor))

    return lista_mayor


def jugadores_mayor_promedio(lista:list, data:str):
    '''
    Esta función recorre una lista de jugadores y encuentra jugadores que tienen el mayor valor en una estadística específica.
    Recibe una lista y un dato
    Retorna una lista de cadenas con los jugadores y los valores correspondientes.
    '''
    jugadores_mayores = []
    promedio_ingresado = ingresar_promedio()

    for jugador in lista:
        promedio_jugador = jugador['estadisticas'][data]
        if promedio_jugador > promedio_ingresado:
            jugadores_mayores.append((jugador['nombre'], promedio_jugador))

    if jugadores_mayores:
        print("Los jugadores con un promedio mayor a {0} son:".format(promedio_ingresado))
        for jugador in jugadores_mayores:
            print("Nombre: {0}, Promedio: {1}".format(jugador[0],jugador[1]))
    else:
        print("No hay jugadores con un promedio mayor a {0}".format(promedio_ingresado))


def ingresar_promedio():
    '''
    Esta función pide al usuario un promedio y lo devuelve.
    '''
    while True:
        promedio_ingresado = input("Ingrese un promedio: ")
        if promedio_ingresado.isdigit():
            promedio_ingresado = float(promedio_ingresado)
            return promedio_ingresado
        else:
            print("Error: Ingrese solo números.")

def maxima_cantidad_logros(lista_jugadores):
    '''
    Esta función recorre una lista de jugadores y encuentra el jugador con la mayor cantidad de logros.
    Recibe una lista de jugadores.
    Retorna una lista de cadenas con los jugadores y los valores correspondientes.
    '''
    valor_maximo = 0

    for jugador in lista_jugadores:
        cantidad_logros = len(jugador["logros"])
        if cantidad_logros > valor_maximo:
            valor_maximo = cantidad_logros
            nombre_jugador_maximo = jugador["nombre"]

    return nombre_jugador_maximo

def imprimir_resultado(resultado: list[str]):
    """
    Esta función imprime los elementos de una lista en líneas separadas.
    Recibe por parámetro una lista de cadenas.
    """
    if resultado:
        for jugador_valor in resultado:
            print(jugador_valor)
    else:
        print("No se encontraron jugadores con la estadística especificada.")




# Función para mostrar el menú
def mostrar_menu():
    print("---- MENU ----")
    print("1. Mostar jugadores y posiciones.")
    print("2. Ver estadisticas de jugador por indice")
    print("3. Crear CSV con el jugador seleccionado en el punto anterior.")
    print("4. Seleccionar un jugador y mostrar sus logros.")
    print("5. Mostrar el promedio de puntos por partido de todo el equipo del Dream Team, ordenado por nombre de manera ascendente")
    print("6. ingresar el nombre de un jugador y mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto")
    print("7. Mostrar el jugador con la mayor cantidad de rebotes totales")
    print("8. Mostrar el jugador con el mayor porcentaje de tiros de campo")
    print("9. Mostrar el jugador con la mayor cantidad de asistencias totales")
    print("10. Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.")
    print("11. Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.")
    print("12. Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.")
    print("13. Mostrar el jugador con la mayor cantidad de robos totales")
    print("14. Mostrar el jugador con la mayor cantidad de bloqueos totales")
    print("15. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.")
    # print("16. Opción 16")
    print("17. Mostrar al jugador con la mayor cantida de logros.")
    print("18. Ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.")
    print("19. Mostrar el jugador con la mayor cantidad de temporadas jugadas")
    # print("20. Opción 20")
    # print("0. Salir")
