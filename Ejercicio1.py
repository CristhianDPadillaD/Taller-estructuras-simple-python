 
# Ejercicio 1
# Autores:
# - Juan David Calpa Lopez
# - Cristhian David Padilla Delgado 

ListaLectura =[]

def agregar_lectura ():
      
    try:
        lectura = int(input("Digite el valor de la lectura "))
        ListaLectura.append(lectura)
    except ValueError as e:
        print("Ingresar un caracter valido")
    except Exception as e:
        print("Error inesperado ", str(e))

def calcular_promedio ():
   if ListaLectura:
        promedio = sum(ListaLectura)/len(ListaLectura)
        return print ("El promedio de las lecturas es de ", promedio)
   else :
       return print("No se puede calcular el promedio porque no se han agregado lecturas")
    
def lectura_maxima ():
    if ListaLectura:
        maximo = max(ListaLectura)
        return print("El valor maximo de una lectura es de ", maximo)
    else :
       return print("No Se puede calcular la lectura maxima por que no se han agregado lecturas")

def lectura_minima():
    if ListaLectura:
        minimo = min(ListaLectura)
        return print("El valor minimo de la lectura es de ", minimo)
    else :
       return print("No se puede calcular la lectura minima por que no se han agregado lecturas")

def cantidad_lecturas ():
    if ListaLectura:
        cantidad = len(ListaLectura)
        return print ("La cantidad de lecturas es de ", cantidad)
    else :
       return print("No Se puede calcular porque no se han agregado lecturas")

x =0
while (x != 6):
    print("*************************************")
    print("1. Ingresar nueva lectura")
    print("2. Calcular promedio de lecturas")
    print("3. Mostrar lectura máxima")
    print("4. Mostrar lectura mínima")
    print("5. Cantidad de lecturas realizadas")
    print("6. Salir")

    # Manejo de error al ingresar algo diferente a un número 
    try:
        x = int(input("Digite la accion a realizar: "))
    except ValueError:
        print("*************************************")
        print("ERROR")
    print("*************************************")

    if x==1:
        agregar_lectura()
    elif x==2:
        calcular_promedio()
    elif x==3:
        lectura_maxima()
    elif x==4:
        lectura_minima()
    elif x==5:
        cantidad_lecturas()
    elif x==6:
        print("Gracias por usar el script")

    else: 
        print("Digite un valor válido ")



