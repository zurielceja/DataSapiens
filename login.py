def login_function():
    if __name__ == "__main__":
        USUARIO = 'zuriel'
        CONTRASENA = 'zuriel'

    # Ahora le toca a la persona interactuando con el programa
    # ingresar un par de usuario-contraseña. Experimenta modificando
    # el texto entre las '' para personalizar la experiencia de usuario
    username = input('Ingrese su nombre de usuario:\n > ')
    password = input('Ingrese la contraseña:\n > ')

    # El último paso para crear un login es comprobar si
    # los datos que ingresaron son válidos o incorrectos.

    # Primero comprobemos los usuarios, podemos comparar
    # directamente el par usuario-contraseña, pero esto nos
    # dará la flexibilidad de hacer cosas interesantes,
    # como decir un mensaje acerca del error que la persona
    # cometió
    if username == USUARIO:
        # En este punto, la persona ingreso correctamente
        # el usuario, comprobemos la contraseña ahora.
        if password == CONTRASENA:
            # La persona que interactua con el programa
            # únicamente verá este mensaje si el par
            # de usuario-contraseña que introdujo son correctos.
            print("############################################################################## \n")
            print("Buen día! Bienvenido al programa, Zuriel")
            print("############################################################################## \n")
        else:
            print("Contraseña erronea")
    else:
        print('El usuario no existe')
        
        return
