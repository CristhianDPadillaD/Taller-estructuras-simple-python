contacto = []
todosContactos = []

def agregarContacto ():
    nombre =input("Digite el nombre del contacto ")
    apellido =input("Digite el apellido del contacto ")
    cedula =input("Digite el cedula del contacto ")
    celular =input("Digite el celular del contacto ")
    correo =input("Digite el correo del contacto ")
    direccion =input("Digite el direccion del contacto ")

    nuevo_contacto = {
        "Nombre": nombre,
        "Apellido": apellido,
        "Cedula": cedula,
        "Celular": celular,
        "Correo": correo,
        "Direccion": direccion
    }

    contacto_resumen = {
        "Nombre": nombre,
        "Cedula": cedula
    }
    contacto.append(nuevo_contacto)
    todosContactos.append(contacto_resumen)
    print("Contacto agregado con éxito.") 

def listarContacto ():
        print (contacto)    

def listarTodosContactos ():
    print (todosContactos)
    


opcion =0
while (opcion != 6):
    print("*************************************")
    print("1. Agregar un contacto")
    print("2. Consultar todos los contactos")
    print("3. Consultar la información de un contacto")
    print("4. Editar información de un contacto")
    print("5. Eliminar un contacto")
    print("6. Salir")
      # Manejo de error al ingresar algo diferente a un número 
    try:
        opcion = int(input("Digite una opcion "))
    except ValueError:
        print("*************************************")
        print("ERROR")
    print("*************************************")

    # Opciones del menu
    if(opcion == 1):
        agregarContacto()
    elif(opcion ==2 ):
        listarTodosContactos()
    elif (opcion ==3):
        listarContacto()
    elif (opcion ==4):
        print("Es la opcion cuatro")
    elif (opcion ==5):
        print("Es la opcion cinco")
    elif (opcion ==6):
        print("Gracias por usar el script 🥵")
    else:
        print("Digite una opcion valida")
