from funciones import *

flag = False
estadisticas_jugador = ""
while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")
    match opcion:
        case "0":
            exit()
        
        case "1":
            print(mostrar_jugador(lista_jugadores,"nombre"))
        
        case "2":
            print(mostrar_jugador(lista_jugadores,"nombre"))
            estadisticas_jugador = obtener_informacion_jugador(lista_jugadores)
            flag = True
        
        case "3":
            if flag == True:
                guardar_csv("jugador.csv",str(estadisticas_jugador))
            else:
                print("Ingrese a la opcion 2 primero")
           
        case "4":
            print(mostrar_jugador(lista_jugadores,"nombre"))
            jugador_encontrado = buscar_jugador_por_nombre(lista_jugadores)
            imprimir_dato(jugador_encontrado,"logros")

        case "5":
            formato_cadena(ordenar_palabra(lista_jugadores,"nombre"),"nombre","promedio_puntos_por_partido")
            print("El promedio total por partido es de: {0}".format(calcular_promedio(lista_jugadores,"promedio_puntos_por_partido")))
        
        case "6":
            print(mostrar_jugador(lista_jugadores,"nombre"))
            jugador_logro = buscar_jugador_por_nombre(lista_jugadores)
            flag = True
            for jugador in jugador_logro:
                print("\n",jugador["nombre"])
                for logro in jugador["logros"]:
                    if "Miembro del Salon de la Fama del Baloncesto" == logro:
                        flag = False
                        print(logro)
                
        case "7":
            rebotes_totales = calcular_mayor(lista_jugadores,"rebotes_totales")
            imprimir_resultado(rebotes_totales)

        case "8":
            porcentaje_tiros_campo = calcular_mayor(lista_jugadores,"porcentaje_tiros_de_campo")
            imprimir_resultado(porcentaje_tiros_campo)

        case "9":
            asistencias_totales = calcular_mayor(lista_jugadores,"asistencias_totales")
            imprimir_resultado(asistencias_totales)

        case "10":
           jugadores_mayor_promedio(lista_jugadores, "promedio_puntos_por_partido")

        case "11":
            jugadores_mayor_promedio(lista_jugadores, "promedio_rebotes_por_partido")

        case "12":
            jugadores_mayor_promedio(lista_jugadores, "promedio_asistencias_por_partido")

        case "13":
           robos_totales = calcular_mayor(lista_jugadores,"robos_totales")
           imprimir_resultado(robos_totales)

        case "14":
           bloqueo_totales = calcular_mayor(lista_jugadores,"bloqueos_totales")
           imprimir_resultado(bloqueo_totales)

        case "15":
            jugadores_mayor_promedio(lista_jugadores,"porcentaje_tiros_libres")

        case "16":
            porcentaje_tiros_campo_sin_menor = calcular_promedio_sin_menor(lista_jugadores,"promedio_puntos_por_partido")
            imprimir_resultado(porcentaje_tiros_campo_sin_menor)

        case "17":
            print(maxima_cantidad_logros(lista_jugadores))

        case "18":
           jugadores_mayor_promedio(lista_jugadores,"porcentaje_tiros_triples")

        case "19":
            cantidad_temporadas = calcular_mayor(lista_jugadores, "temporadas")
            imprimir_resultado(cantidad_temporadas)

        # case "20":
        #     print("Ha seleccionado la Opción 20")
        case _:
            print("Opción inválida. Intente de nuevo.")

    clearconsole()