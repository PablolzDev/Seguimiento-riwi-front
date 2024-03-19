"""Descripción del Problema:
Una tienda en línea desea implementar una calculadora de descuentos para sus
clientes. El negocio ofrece descuentos basados en la cantidad de artículos que el
cliente compra. Se aplican descuentos diferentes según la cantidad de artículos
comprados.
Requisitos del Problema:
Entrada de Datos: El programa debe solicitar al usuario que ingrese la cantidad de
artículos que desea comprar.
Calcular Descuento: El programa debe calcular el descuento aplicable según la
cantidad de artículos comprados, utilizando la siguiente tabla:
● Si el cliente compra menos de 5 artículos, no se aplica ningún descuento.
● Si el cliente compra entre 5 y 10 artículos (inclusive), se aplica un descuento
del 5%.
● Si el cliente compra entre 11 y 20 artículos (inclusive), se aplica un
descuento del 10%.
● Si el cliente compra más de 20 artículos, se aplica un descuento del 15%.
Mostrar Resultado: El programa debe mostrar el descuento aplicado y el monto
total a pagar después de aplicar el descuento correspondiente."""

#Se pide tanto el monto total y la cantidad de los articulos
cantidad = int(input("Ingrese la cantidad de articulos a pagar")) 
monto = int(input("Ingrese el monto total"))
 
def calcular_descuentos(cantidad, monto):#la funcion recibe esta informacion con los parametros
  if cantidad < 5:  #Se realizan las validaciones de los des cuentos , dependiendo de que cantidad de articulos tenga
    print("No se aplica ningun descuento ")
  elif cantidad >= 5 and cantidad <=10: #Aplica el 5% de descuento y lo muestra
    descount1 = monto * 5/100
    print(f"El descuento fue del 5% :{descount1} ")
  elif cantidad >= 11 and cantidad <=20:#Aplica el 10% de descuento y lo muestra
    descount2 = monto * 10/100
    print(f"El descuento fue del 10% :{descount2} ")
  elif cantidad >20:#Aplica el 15% de descuento y lo muestra
    descount3= monto * 15/100
    print(f"El descuento fue del 15% :{descount3} ")

calcular_descuentos(cantidad,monto) #imprimimos la funcion, con la informacion que los parametros van a recibir




  