 id = int (input("Digite la cedula del contacto que desea buscar: "))
        for contactoActual in contacto:

            if contactoActual["Cedula"] == id:
                    print("Información del contacto:")
                    print("Nombre:", contactoActual["Nombre"])
                    print("Apellido:", contactoActual["Apellido"])
                    print("Cédula:", contactoActual["Cedula"])
                    print("Celular:", contactoActual["Celular"])
                    print("Correo:", contactoActual["Correo"])
                    print("Dirección:", contactoActual["Direccion"])
                    
                    break
            else:
                print("No se encontró ningún contacto con la cédula proporcionada")