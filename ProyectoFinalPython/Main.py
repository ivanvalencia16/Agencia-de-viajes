from BaseDeDatos import Destinos_Colombia
from BaseDeDatos import Precio_Destinos
import Registro as ik

ik.login()

def inicio1():
    # Saludo de bienvenida y elección de destino
    
    print("Bienvenido a nuestra agencia de viajes\n")
    print("Esta es la lista de destinos disponibles:\n")

    # Mostrar destinos con numeración
    for i, destino in enumerate(Destinos_Colombia.keys(), 1):
        print(f"{i}. {destino}")

    # Solicitamos al usuario que ingrese su lugar de destino por número o nombre
    entrada_usuario = input("\nPor favor, ingrese el número o nombre de su lugar de destino:\n").capitalize()

    # Convertir la entrada en el nombre del destino si es un número
    if entrada_usuario.isdigit():
        indice = int(entrada_usuario) - 1
        if 0 <= indice < len(Destinos_Colombia):
            Lugar_Destino = list(Destinos_Colombia.keys())[indice]
        else:
            print("\nNúmero de destino no válido.")
            return
    else:
        Lugar_Destino = entrada_usuario

    # Preguntamos si el usuario quiere continuar con esta ciudad
    while True:
        confirmacion = input(f"\n¿Te gustaría continuar con {Lugar_Destino}? (Si/No):\n").capitalize()
        if confirmacion == 'Si':
            inicio2(Lugar_Destino)
            break
        elif confirmacion == 'No':
            print("\nVolvamos a empezar.\n")
            inicio1()
            break
        else:
            print("\nOpción no válida. Por favor ingresa 'Si' o 'No'.")

def inicio2(Lugar_Destino):
    # Verificamos si el destino ingresado está en el diccionario
    if Lugar_Destino in Destinos_Colombia:
        # Extraemos la lista de hoteles para el destino seleccionado
        hoteles = list(Destinos_Colombia[Lugar_Destino].keys())
        print(f"\nEstos son los hoteles disponibles en {Lugar_Destino}:\n")
        for i, hotel in enumerate(hoteles, 1):
            print(f"{i}. {hotel}")

        # Bucle para permitir al usuario seleccionar un hotel hasta que acepte las actividades
        while True:
            # Solicitamos al usuario que elija un hotel por número o nombre
            entrada_hotel = input("\nIngresa el número o nombre del hotel que quieres reservar:\n").capitalize()

            # Convertir la entrada en el nombre del hotel si es un número
            if entrada_hotel.isdigit():
                indice_hotel = int(entrada_hotel) - 1
                if 0 <= indice_hotel < len(hoteles):
                    Hotel = hoteles[indice_hotel]
                else:
                    print("\nNúmero de hotel no válido.")
                    continue
            else:
                Hotel = entrada_hotel
            if Hotel in Precio_Destinos:
                inicio3(Hotel, Lugar_Destino)
                break
            else:
                print("\nEste hotel no está registrado.\n")
    else:
        print("\nEste lugar no existe.\n")

def inicio3(Hotel, Lugar_Destino):
    # Verificamos si el hotel está en la lista de precios
    if Hotel in Precio_Destinos:
        # Mostramos las actividades disponibles para el hotel seleccionado
        actividades = ', '.join(Destinos_Colombia[Lugar_Destino][Hotel])
        print(f"\nLas actividades disponibles en el hotel {Hotel} son:\n{actividades}")

        # Preguntamos si el usuario quiere continuar con este hotel
        confirmacion = input("\n¿Te gustaría reservar en este hotel? (Si/No):\n").capitalize()
        if confirmacion == 'Si':
            # Pedimos el número de noches
            Dias = int(input("\nIngresa el número de noches que quieres reservar:\n"))
            # Pedimos la cantidad de personas que van a reservar
            Personas = int(input("Numero de personas que viajan\n"))

            # Calculamos el total a pagar multiplicando las noches por el precio del hotel
            Total = Dias * Precio_Destinos[Hotel] * Personas

            # Formateamos el total con separadores de miles y sin decimales
            Total_formateado = f"{Total:,}"
            # Imprimimos la CANTIDAD TOTAL 
            print(f"\nEl total por {Dias} noches en el hotel {Hotel} es: {Total_formateado} COP\n")
            
            # Preguntamos si el usuario desea continuar PARA GENERAR RECIBO
            confirmacion6 = input("¿Deseas continuar? (Si/No):\n").capitalize()
            if confirmacion6 == 'Si':
                # Almacenamos los datos de las personas
                datos_personas = []
                # Pedimos la fecha de viaje
                fecha_viaje = input("\n¿En qué fecha deseas realizar el viaje? (DD/MM/AAAA):\n")
                # Creamos un bucle para repetir el mensaje por la cantidad de personas que van a reservar
                for i in range(Personas):
                    nombre = input(f"\nIngresar el nombre de la persona {i+1}:\n")
                    cedula = input(f"Ingresar el número de cédula de {nombre}:\n")
                    # Agregamos los datos a la lista
                    datos_personas.append((nombre, cedula))
                    # Confirmamos la reserva 
                    confirmacion_reserva = input(f"\n¿Estas seguro de realizar esta reserva? (Si/No):\n").capitalize()
                if confirmacion_reserva == 'Si':
                    # Calculamos el valor a pagar por cada persona a partir del total mostrado
                    Total_definitivo= Total// Personas
                    #Formateamos el valor para separarlo con , 
                    Total_formateado2 = f"{Total_definitivo:,}"
                    # Imprimimos los recibos por persona
                    print(f"\nDetalles de la reserva:\n\nFecha: {fecha_viaje}\nPersonas:{Personas}\n")
                    # Bucle que genera los recibos con los datos almacenados y el valor por persona
                    for nombre, cedula in datos_personas:
                        print(f"Nombre: {nombre}, Cédula: {cedula}")
                        print(f"Precio total: ${Total_formateado2}")
                        print("Gracias por elegirnos.\n")
                    # Despues de ingresar los datos 
                    else:
                        print("Reserva realizada.")
                # Si decidimos retractarnos despues de ver el precio y decimos no, termina el bucle
                elif confirmacion6 == 'No':
                    print("\nGracias por visitarnos y elejirnos.")
        elif confirmacion == 'No':
                print("\nVamos a intentar con otro hotel.\n")
                inicio2(Lugar_Destino)
        else:
            print("\nOpción no válida. Por favor ingresa 'Si' o 'No'.")
            inicio3(Hotel, Lugar_Destino)
    else:
        print("\nEste hotel no está registrado.\n")

inicio1()




