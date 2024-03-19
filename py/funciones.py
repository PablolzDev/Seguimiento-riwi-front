def Actualice_product(updates, diccionario):
  new_product = input("Ingrese el producto a actualizar")
  new_prince = int(input("Ingrese el nuevo precio"))
  updates = diccionario.update({new_product:new_prince}) 
