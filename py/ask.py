lista_empleados = []


########################### agregar empleados ######################
def agrega_empleados(lista): #recibimos el parametro de la lista
  respuesta = input("¿Quieres ingresar empleados? (si/no): ") #Pregunta para revisar si ingresara mas tareas

  while respuesta.lower() == "si": # si la persona responde si, ya sea en Mayus o Min, entra a pedir los datos
    nuevoe = input("Ingrese el nombre del empleado : ").lower()
    id = int(input("Ingrese su identificacion : "))
    cargo = input("Ingrese su cargo : ")
    lista.append({"nombre": nuevoe, "identificacion": id , "cargo": cargo}) #Luego de pedir los datos, se agregan los datos a la lista
    print("Agregando...")
    respuesta = input("¿Quieres agregar otro empleado? (si/no): ") # si la persona no quiere ingresar mas empleados que simplemente responda no
    print("Tu respuesta fue:", respuesta)
  else:# este else es para cuando la persona responda no, no cerrar el bucle y cerrar la aplicacion, si no retornar a el menu
    menu_empleados()    
  


############# Eliminar empleados ##############
def eliminar_empleados(lista):
  empleadox = input("Ingrese el nombre del empleado que desea eliminar : ")
  id = int(input("Ingrese su identificacion a eliminar : "))
  cargo = input("Ingrese su cargo a eliminar : ") # se ingresan los datos para saber especificamente que eliminar
  index = lista.index({"nombre" : empleadox , "identificacion" : id   ,"cargo" : cargo}) # EN el .index buscamos la posicion de los datos ingresados 
  lista.pop(index) # una vez ingresados, se eliminan basado en su index
  print("Eliminando...")

########################## Modificar empleados ##############
def modificar_empleados(lista):
  empleadox = input("Ingrese el nombre del empleado: ")
  id = int(input("Ingrese su identificacion: "))
  cargo = input("Ingrese su cargo a modificar : ") # se piden los datos, pero en este caso solo pasaremos a modificar el cargo del empleado
  index1 = lista.index({"nombre" : empleadox , "identificacion" : id   ,"cargo" : cargo}) # hace lo mismo de buscar el index de la lista
  cargo_mod= input("Ingrese el nuevo cargo : ")
  lista[index1] = {"nombre" : empleadox , "identificacion" : id   ,"cargo" : cargo_mod}# se le pide un nuevo dato y se remplaza en el index encontrado
  print("Modificando...")
 
############ imprimimos empleados ############ 
def imprimimos_empleados(lista):  # no se como funciona xd 
  print(lista)
  if not lista: #Si la lista no tiene contenido se imprime
        print("No hay empleados en la lista.")
  else:
        print("Lista de empleados:") # les debo la exlicacion
        for i, empleados in enumerate(lista, 1):
            emp = "nombre" if empleados["nombre"] else "No esta"
            print(f"{i}. -{empleados} - Cargo: {emp}")


############### Menu ###########
def menu_empleados():
  print(f""" 1. Ingresar empleado
             2. Modificar empleado
             3. Eliminar empleado
             4. Mostrar empleados
             5. Salir del sistema""")   # Se dan las opciones
  
  #El ciclo infinito que reproduce el menu
  while True:
    op = int(input("Ingrese la opcion que desea hacer :"))
    if op ==1: # Esta opcion lo lleva a ingresar empleado
     agrega_empleados(lista_empleados)
    elif op == 2: # Esta opcion lo lleva a modificar empleado
     modificar_empleados(lista_empleados)
    elif op == 3: # Esta opcion lo lleva a eliminar empleado
     eliminar_empleados(lista_empleados)
    elif op == 4: # Esta opcion lo lleva a mostrar los empleados
     imprimimos_empleados(lista_empleados)
    elif op == 5:
      print("!Hasta luego¡")
    break # en esta opcion si ingresa 5, con el break te saca del ciclo infinto




menu_empleados() #imprime el menu de empleados con sus metodos