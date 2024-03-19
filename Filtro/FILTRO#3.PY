"""Descripción del Problema:
Escribe un programa en Python que ayude a calcular la propina a dejar en un
restaurante. El programa debe permitir al usuario ingresar el total de la cuenta y
calcular la propina basada en un porcentaje de 12%.
Requisitos del Problema:
Entrada de Datos: El programa debe solicitar al usuario que ingrese el total de la
cuenta en el restaurante.
Calcular Propina: El programa debe calcular la propina basada en el total de la
cuenta y el porcentaje de propina equivalente al 12%.
Mostrar Resultado: El programa debe mostrar al usuario el monto de la propina
calculada."""

totalCuenta = int(input("Ingrese el total de su cuenta por favor : "))

def calcular_propina(totalCuenta): #la funcion recibe en el parametro el dato de total cuenta
  montoPropina = totalCuenta*12/100 #se calcula el porcentaje basado en el total
  print(f"El monto de la propina fue :{montoPropina} ") # se muestra el resultado de el calculo
 
calcular_propina(totalCuenta) #se ejecuta la funcion recibiendo el dato de total cuenta