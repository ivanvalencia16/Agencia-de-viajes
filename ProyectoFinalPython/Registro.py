##Base de datos usuarios
datosUsuarios = {
    "Juan": ["Loco", "jhones2006hotmail.es", "3155860495" ""],
    "Pedro": ["Juan", "loco2006hotmail.es", "3166407217" ""]
}

##Funcion que alberga los datos para registro usuarios 
def Registrarse():
    ##Bucle registro nuevo usuario
    while True:
        ##Ingresar el nuevo usuario
        nuevoUsuario = input("Ingrese su nuevo usuario:\n")
        ##Si el nuevo usuario ya esta, se repite el bucle
        if nuevoUsuario in datosUsuarios:
            print("El usuario ya existe. ")
        ##Si el usuario no existe, le pide la contrasena nueva
        else:
            ##Bucle para registrar la contrasena nueva,correo y numero
            while True:                   
                nuevaContrasena = input("Ingrese su nueva contraseña (Debe contener minimo 6 caracteres de cualquier tipo):\n").strip()
                ##Si la contrasena nueva es menor a x caracteres, vuelve a pedirsela
                if len(nuevaContrasena) < 6:
                    print("La contraseña debe tener al menos 6 caracteres.")
                    return False
                ##Si la contrasena es mayor a x caracteres, le pide el correo y el numero
                else:
                    correo = input("Ingrese su correo electrónico:\n")
                    numero = input("Ingrese su número de teléfono:\n")
                    ##El usuario tambien debera enlazar una tarjeta para realizar sus pagos
                    numeroTarjeta=input("Ingresa el numero de tu cuenta bancaria: ")
                    pwTarjeta=input("Ingresa tu contraseña (***): ")
                    nombrePropietario=input("Ingresa el nombre del propietario: ")
                    fechaLimite=input("Ingresa la fecha de vencimiento: ")
                    tarjetaUsuario= numeroTarjeta, pwTarjeta, nombrePropietario, fechaLimite
                    ##Los nuevos datos se almacenaran en la base de datos
                    datosUsuarios[nuevoUsuario] = [nuevaContrasena, correo, numero, tarjetaUsuario]
                    print("Registro exitoso")
                    return True

##Funcion que alberga los datos y condicionales necesarios para iniciar sesion
def iniciarSesion():
    ##Numero de intentos maximos para ingresar 
    intentosMaximos=1
    ##Bucle en el que pedira los datos en un maximo de x intentos
    for intentos in range(intentosMaximos):
        usuario = input("Ingresa tu nombre de usuario:\n")
        contrasena = input("Ingresa tu contrasena:\n")
            
        ##Si los datos ingresados por el usuario estan registrados en la base de detos, puede continuar
        if usuario in datosUsuarios and datosUsuarios[usuario][0] == contrasena:
            print("Bienvenido")
            return True
        else:
            print("Contraseña o nombre de usuario incorrectos ")
            return False
    ##Si el usuario agota los intentos, puede elegir registrarse o esperar para volver a intentar ingresar
    irRegistro=str(input("Has agotado el numero maximo de intentos, ¿deseas registrarte? (Si/No):\n")).capitalize()
    ##Si el usuario elige registrarse, sera llevado a la funcion Registrarse para ingresar sus datos a nuestra base
    if irRegistro == "Si":
            Registrarse()
    else: 
        print("Intentalo de nuevo mas tarde")
        return False
    
#Funcion que contiene las funciones de iniciar sesion y registrarse
def login():
    #Hasta que no retorne alguna de las funciones True; no terminara el bucle 
    while True:
        ##El usuario elige entre alguna de estas dos opciones para poder acceder a los planes
        inicio0=str(input("1.Deseas iniciar sesion o 2.registrarte (1/2)\n"))

        if inicio0 == "1": 
            if iniciarSesion():
                break
        elif inicio0 == "2":
            if Registrarse():
                break

        ##Si el numero ingresado no es 1 o 2, imprimira este mensaje indicando que no es valido
        else:
            print("Numero no valido")


