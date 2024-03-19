#GESTION DE INVENTARIO DE UNA TIENDA

nombres = []
Precios = []
Cantidad = []

def Agregar_Producto():
  ###############Se piden los datos de las listas###################
  nombre_producto = input("Ingrese el nombre de el producto")
  nombres.append(nombre_producto)#Va agregando valores en la lista
  precio_producto = int(input ("Ingrese el precio unitario del producto"))
  Precios.append(precio_producto)#Va agregando valores en la lista
  Cantidad_producto = input("Ingrese la cantidad que tendra el producto")
  Cantidad.append(Cantidad_producto)#Va agregando valores en la lista

  return nombre_producto, precio_producto, Cantidad_producto

  



def productos_Nuevos():
  #####Se hace 3 ciclo for, uno para recorrer cada lista y que muestre los productos ingresados ################################
  for elementosn in nombres: #Recorre cada elemento y lo muestra
    print(f"El producto son : {elementosn}")#Recorre cada elemento y lo muestra
  for elementosp in Precios:
    print(f"Su precio es : {elementosp}")#Recorre cada elemento y lo muestra
  for elementosc in Cantidad:
    print(f"Y su cantidad es {elementosc}")#Recorre cada elemento y lo muestra
  




def remplazar_productos():
  #########Remplazamiento de los productos###################################
  new_product = input("Ingrese el nombre del nuevo producto a remplazar")
  nombres[0] = new_product

  new_precio = int(input("Ingrese el nuevo precio del producto"))
  Precios[0] = new_precio

  new_cantidad = int(input("Ingrese la nueva cantidad del producto"))
  Cantidad[0] = new_cantidad

  print(f"El nuevo producto es : {new_product}")
  print(f"Los nuevos precios son : {new_precio}")
  print(f"La nueva cantidad es : {new_cantidad} ")

  return new_product, new_precio, new_cantidad


def eliminar_productos(nombre_producto):
  ###################Eliminar productos especificos################### 
  nombre_borrar = input("Ingrese el nombre del nuevo producto a remplazar")
  Agregar_Producto()

  if nombre_borrar == nombre_producto:
    (f"El producto fue borrado satisfactoriamente {nombres}")
  
 


  precio_borrar = int(input ("Ingrese el precio unitario del producto"))
  
  Cantidad_borrar = input("Ingrese la cantidad que tendra el producto")
  
  nombres.remove
  





          
  
  """#Listamiento de los productos con su valor principal
  #for nombre_producto, precio_producto in Inventario.items():
 #   print(f"El Nombre del producto es {nombre_producto} y el valor de este")

  """##Actualizamos el diccionarioo



"""
  #Y con sus valores actualizados
  for nombre_producto, precio_producto in Inventario.items():
    print(f"El Nombre del producto es {nombre_producto} y el nuevo valor de este{precio_producto}")
  
  #Eliminar un producto del diccionario
  #print(Inventario.clear(nombre_producto,precio_producto))("Prodcuto Eliminado con exito")

  #Verificacion de producto en el inventario
  nombreV = input("Busque el producto por su nombre")
  precioV = int(input("Busque el producto por su precio"))

  for nombre_producto,precio_producto in Inventario.items():
    if nombreV == nombre_producto:
      print(f"Este es el producto seleccionado : {nombre_producto}")  
    else:
      precioV = int(input("Busque el producto por su precio"))

    if precioV == precio_producto:
      print(f"Este es el producto seleccionado : {precioV} ")
    else:
      print("El producto que buscas no ha sido registrado aun!!")
    
  

Agregar_Producto()


"""

Agregar_Producto()
eliminar_productos()