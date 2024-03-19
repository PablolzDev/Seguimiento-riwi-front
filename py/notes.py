inventario={}


def actualizar_inventario():

    name=str(input("Ingrese el nombre del producto a actualizar ") )     
    if name in inventario: #BUSCAMOS EL NOMBRE INGRESADO EN LAS KEYS DEL DICCIONARIO
        inventario.pop(name) #ELIMINAMOS LA LLAVE Y LOS VALORES
        print("Ahora ingresa los nuevos datos: ")
    else: 
        print("El elemento no esta en el inventario ")
    agregar_inventario()#INGRESAMOS NUEVAMENTE EL PRODUCTO CORRIGIENDO ERRORES 
    

def agregar_inventario():

    name = str(input("Ingrese el nombre del producto "))
    cant = int(input("Ingrese la cantidad "))#SOLICITAMOS LOS DATOS PARA INGRESAR UN PRODUCTO
    price = float(input("Ingrese el precio "))

    inventario[name]=(cant,price) #CREAMOS EL DICCIONARIO CON LOS DATOS SUMINISTRADOS
    return name,cant,price


def eliminar_inventario():

    print(inventario.keys())#MOSTRAMOS AL USUARIO LOS NOMBRES QUE YA TIENE EL DICCIONARIO
    name = str(input("Ingrese el nombre del objeto que desea eliminar "))
    if name in inventario:#REVISAMOS SI EL NOMBRE INGRESADO ESTA EN EL DICCIONARIO
        inventario.pop(name)#ELIMINAMOS EL ELEMENTO
        
    

def verificar_inventario():

    name=str(input("Ingrese el nombre del producto que busca "))
    if name in inventario.keys(): #BUSCAMOS EL ELEMENTO EN TODAS LAS LLAVES DEL DICCIONARIO PARA VER SI EXISTE DENTRO DEL MISMO
            print("El producto",name,"se encuentra en el inventario ")
    else:
        print("El producto",name,"no se encuentra en el inventario ")
    return inventario

def listar_inventario():
    for x, y in inventario.items():
        print(x, y)
    return inventario


def menu():

    opcion= int(input("""Ingrese un numero para continuar:

               (1) Agregar un nuevo producto al inventario.
               (2) Actualizar la cantidad de un producto existente en el inventario.
               (3) Eliminar un producto del inventario.
               (4) Veriﬁcar si un producto especíﬁco está en el inventario.
               (5) Listar todos los productos en el inventario.
               (6) Apagar el programa
                Su respuesta es: """))
    while opcion > 0 and opcion<7:
        if opcion== 1:
            print(agregar_inventario())
            menu()
        elif opcion == 2:
            print(actualizar_inventario())
            menu()
        elif opcion == 3:
            print(eliminar_inventario())
            menu()
        elif opcion == 4:
            print(verificar_inventario())
            menu()
        elif opcion== 5:
            print(listar_inventario())
            menu()
        elif opcion == 5:
            break

menu()