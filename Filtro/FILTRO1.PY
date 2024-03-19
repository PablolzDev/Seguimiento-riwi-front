"""Descripción del Problema:
Una familia necesita una aplicación para gestionar su lista de compras semanal.
Cada semana, la familia elabora una lista de productos que necesitan comprar en
el supermercado. La aplicación debe permitir a los usuarios agregar, modificar,
eliminar, listar y buscar productos de manera eficiente.
Requisitos del Problema:
● Agregar Producto: Los usuarios deben poder agregar un nuevo producto a
la lista de compras. Cada producto debe incluir un nombre descriptivo, una
cantidad requerida y, opcionalmente, una nota adicional.
● Modificar Producto: Los usuarios deben tener la capacidad de modificar un
producto existente en la lista de compras. Esto incluye cambiar la cantidad
requerida o la nota adicional asociada al producto.
● Eliminar Producto: Los usuarios deben poder eliminar un producto existente
de la lista de compras si ya no es necesario.
● Listar Productos: Se debe poder mostrar una lista de todos los productos
en la lista de compras, incluyendo detalles como el nombre del producto, la
cantidad requerida y la nota adicional.
● Buscar Productos: Los usuarios deben poder buscar un producto específico
en la lista de compras utilizando su nombre o cualquier otro criterio
relevante."""

lista_compras_semanal = []

def agregar_productos(lista):#recibimos el parametro de la lista

  respuesta = input("¿Desea agregar productos a su lista de compras semanal? (si/no) :")#Pregunta para revisar si ingresara mas tareas 
  
  while respuesta.lower() == "si":# si la persona responde si, ya sea en Mayus o Min, entra a pedir los datos
    nombre_producto = input("Ingrese el nombre del producto que desea agregar :")
    cantidad_producto = int(input("¿Cuanta cantidad tiene de el producto? :"))
    nota_adicional = input("Agregue una nota adicional :")
    semana = int(input("Ingrese la semana que corresponde a la lista"))
    lista.append({"nombre": nombre_producto, "cantidad": cantidad_producto, "nota":nota_adicional, "semana": semana})#Luego de pedir los datos, se agregan los datos a la lista
    print("Registrando...")
    respuesta = input("Desea ingresar mas productos? (si/no) :")# si la persona no quiere ingresar mas empleados que simplemente responda no
  else:# este else es para cuando la persona responda no, no cerrar el bucle y cerrar la aplicacion, si no retornar a el menu
    menu()



def modificar_productos(lista): ####arreglar
  mod_p = input("Que desea modificar la cantidad o la nota? : (nota/cantidad) :") #se pregunta que desea modificar en especifico

  if mod_p == "nota": #si el usuario desea cambiar nota, se hace todo su procedimiento
    print("Ingresara los datos de su producto, para luego modificar lo pedido")
    np_mod = input("Ingrese el nombre de el producto  : ")
    cp_mod = int(input("Ingrese la cantidad de el producto  : "))
    na_mod = input("Ingrese la nota de su producto : ")
    semana_mod = int(input("Ingrese la semana que corresponde a la lista")) #se piden los datos que hay en la lista
    index = lista.index({"nombre" : np_mod, "cantidad" : cp_mod, "nota" : na_mod, "semana": semana_mod})# Y con los datos ingresados, el .index buscara un indice con los datos ingresados
    nal_mod = input("Ingrese la nueva nota para su producto : ") #se pide la informacion a modificar
    lista[index] = {"nombre" : np_mod, "cantidad" : cp_mod, "nota" : nal_mod , "semana": semana_mod}#luego de pedir el dato se remplaza en el index encontrado
    print("Modificando")
    menu()
   #Hace la misma operacion que el caso de arriba, pero solo cuando el usuario ingresa cantidad
  elif mod_p == "cantidad":
    print("Ingresara los datos de su producto, para luego modificar lo pedido")
    np_mod = input("Ingrese el nombre de el producto a modificar : ")
    cp_mod = int(input("Ingrese la cantidad de el producto a modificar : "))
    na_mod = input("Ingrese la nota de su producto : ")
    semana_mod = int(input("Ingrese la semana que corresponde a la lista"))
    index1 = lista.index({"nombre" : np_mod, "cantidad" : cp_mod, "nota" : na_mod, "semana": semana_mod})
    cpo_mod = int(input("Ingrese la nueva cantidad para su producto : ")) 
    lista[index1] = {"nombre" : np_mod, "cantidad" : cpo_mod, "nota" : na_mod, "semana": semana_mod}
    print("Modificando....")
    menu()
  else:
    print("Ingreso invalido, intente de nuevo")
    menu()

def eliminar_producto(lista):
   np_delete= input("Ingrese el nombre del producto que desea eliminar : ")
   cantidad_producto = int(input("Ingrese la cantidad del producto a eliminar : "))
   nota_adicional = input("Ingrese su la nota del producto a eliminar : ") 
   semana_mod = int(input("Ingrese la semana que corresponde a la lista"))# se ingresan los datos para saber especificamente que eliminar
   indexd = lista.index({"nombre" : np_delete , "cantidad" : cantidad_producto  ,"nota" : nota_adicional, "semana" : semana_mod}) # EN el .index buscamos la posicion de los datos ingresados 
   lista.pop(indexd) # una vez ingresados, se eliminan basado en su index
   print("Eliminando...")
   menu()

def imprimimos_productos(lista): #uso un print de la lista basico
  print(lista)


def buscar_producto(lista):
    name = input("Ingrese el nombre del producto que busca ")#Le pedimos a el usuario que ingrese el nombre del producto que desea 
    for i,producto in enumerate(lista, 1): # en este for con el metodo enumerate producto recorre la lista, pero enumerate recorre la lista y convierte lo que recorre en tuplas
     if producto["nombre"] == name : #si producto encontro una key "nombre" igual al dato ingresado
      print(f"el producto esta en la lista :{name}")#se mostrara que fue encontrado
      pass
    menu()
       

def menu():#Crea el menu de opciones para el usuario
  while True: #El true hace que el bucle se vuelva infinito, para que siempre se muestren las opciones
    print(f""" 1. Agregue su producto
               2. modifique su producto
               3. Elimine su producto
               4. imprima la lista de productos
               5. buscar un producto """)   #se crea el menu de opciones
    
    op = int(input("Ingrese la opcion que desea hacer :"))
    if op ==1: # Esta opcion lo lleva a agregar productos
     agregar_productos(lista_compras_semanal)
    elif op == 2: # Esta opcion lo lleva a modificar los productos
     modificar_productos(lista_compras_semanal)
    elif op == 3: # Esta opcion lo lleva a eliminar los productos
     eliminar_producto(lista_compras_semanal)
    elif op == 4: # Esta opcion lo lleva a mostrar los productos
     imprimimos_productos(lista_compras_semanal)
    elif op == 5:# Esta opcion lo lleva a buscar producto
      buscar_producto(lista_compras_semanal)
    elif op == 6: # Y esta ultima lo saca de la aplicacion
      print("!Hasta luego¡")
    break # en esta opcion si ingresa 5, con el break te saca del ciclo infinto 
             

menu() # se ejecuta el menu