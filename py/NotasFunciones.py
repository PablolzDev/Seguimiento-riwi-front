""" CODIGO apoyo clase funciones """



""" Elementos de una funcion """


def mi_funcion(parametro1, parametro2):
    # Cuerpo de la función
    # Puede contener cualquier número de declaraciones
    pass



# Hay funciones integradas de Python len() sum() sort()


""" Ejemplo 1 """


suma_sin_funcion = 3 + 4
print(suma_sin_funcion)



def sumar_numeros_encapsulado(a, b):
    suma = a + b
    return suma

# Llamada a la función
resultado = sumar_numeros_encapsulado(3, 4)
print("El resultado de la suma es:", resultado)



""" Ejemplo 2 """

lista_numeros = [1, 2, 3, 4, 5]
suma = sum(lista_numeros)

lista_notas = [3.5, 4, 3, 4.5, 5]


def sumar_lista_encapsulado(lista):
    suma = sum(lista)
    return suma

# Llamada a la función
numeros = [1, 2, 3, 4, 5]
resultado = sumar_lista_encapsulado(numeros)
print("La suma de la lista es:", resultado)



""" Ejemplo 3 """


def calcular_promedio(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    return promedio

lista_numeros = [10, 20, 30, 40, 50]
promedio = calcular_promedio(lista_numeros)
print("El promedio de la lista es:", promedio)



""" Ejemplo 4 """


def es_palindromo(cadena):
    # Convertir la cadena a minúsculas y eliminar espacios en blanco
    #cadena = cadena.lower().replace(" ", "")
    cadena = cadena.replace(" ", "").lower()
    # Comparar la cadena original con su reverso
    return cadena == cadena[::-1] # invierete la cadena


palabra = "reconocer"
resultado = es_palindromo(palabra)
if resultado:
    print(f'La palabra "{palabra}" es un palíndromo.')
else:
    print(f'La palabra "{palabra}" no es un palíndromo.')



""" Ejemplo 5 """



def invertir_lista(lista):
    return lista[::-1]

# Ejemplo de uso de la función
mi_lista = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista(mi_lista)
print("Lista original:", mi_lista)
print("Lista invertida:", lista_invertida)





#Problemas de funciones

# Problema 1: Contar la cantidad de palabras en una cadena

'''def contar_palabras(cadena):
    # Dividir la cadena en palabras usando espacios en blanco como separadores
    palabras = cadena.split()
    # Contar la cantidad de palabras
    cantidad_palabras = len(palabras)
    return cantidad_palabras

# Ejemplo de uso de la función
texto = "Esta es una cadena"
cantidad = contar_palabras(texto)
print("Cantidad de palabras en la cadena:", cantidad)


# Problema 2: Verificar si una cadena es palindromo

# Problema 3: Contar la cantidad de vocales en una cadena






def contar_vocales(cadena):
    # Convertir la cadena a minúsculas para hacer la búsqueda de vocales insensible a mayúsculas
    cadena = cadena.lower()
    # Inicializar un contador para las vocales
    cantidad_vocales = 0
    # Definir un conjunto de vocales
    vocales = {'a', 'e', 'i', 'o', 'u'}
    # Iterar sobre cada carácter en la cadena
    for caracter in cadena:
        # Verificar si el carácter es una vocal
        if caracter in vocales:
            cantidad_vocales += 1
    return cantidad_vocales

# Ejemplo de uso de la función
texto = "Python es un lenguaje de programación"
cantidad = contar_vocales(texto)
print("Cantidad de vocales en la cadena:", cantidad)



"""
Problema 4: Crear una funcion para registrar documento, por supuesto crear los input que le pida la informacion
"""
'''
nombre=input("Escribe tu nombre: ")
documento=int(input("Escribe tu documento: "))

def recolectarInformacion(nombre,documento):
    return print(f"Hola {nombre} con numero de documento {documento}")

persona1=recolectarInformacion(nombre,documento)

# Problema 5: Crear una funcion para agregar el IVA de un producto 19%

# Problema 5: Crear una funcion para hacer un decsuento de 5% si el cliente compra 5 o mas productos

# Problema 6: Calcular saldo restante de un salario de $2.000.000 despues de gastos por $1.000.000
"""
EJERCIIO 

#HAREMOS LOS DATOS DE LA FACTURA

ProductosV = {}

def info_usuario():

  name = input("Ingrese su nombre ")
  documment = int(input("Ingrese su documento "))
  lastname = input("Ingrese su apellido ")

  return name, documment, lastname

def reg_producto(diccionario):
  nproduct = input("Ingrese el nombre del producto")
  vproduct = int(input("Ingrese el valor de su producto"))
  ProductosV[nproduct] = vproduct
  return ProductosV , nproduct , vproduct
 
def listar (diccionario):
  for x in ProductosV:
    print(x,ProductosV[x])
    return ProductosV
"""
def Casos_descuentos(numProducto):
    reg_producto()
    if reg_producto().nproduct >=3 and reg_producto().nproduct<=4: 
       porcentaje5 = (reg_producto(ProductosV) * 5)/100
       print("Los productos aplican un descuento del 5'%'" , porcentaje5)
    elif reg_producto() >= 5 and reg_producto() <=6 :
        porcentaje10 = ((reg_producto(ProductosV) * 10)/100)
        print("el producto tiene 10'%'")
    elif reg_producto(): 
 """       
         
    

"""
def factura():
  info_usuario.name
  print(info_usuario.name)
  reg_producto()
  print(reg_producto)
  """


info_usuario()
reg_producto()
listar()
print(info_usuario)
print(reg_producto)
print(listar)
#print(Casos_descuentos)
#nombreprod , valorprod = reg_producto
EJERCIIO 

#HAREMOS LOS DATOS DE LA FACTURA

ProductosV = {}

def info_usuario():

  name = input("Ingrese su nombre ")
  documment = int(input("Ingrese su documento "))
  lastname = input("Ingrese su apellido ")

  return name, documment, lastname

def reg_producto(diccionario):
  nproduct = input("Ingrese el nombre del producto")
  vproduct = int(input("Ingrese el valor de su producto"))
  ProductosV[nproduct] = vproduct
  return ProductosV , nproduct , vproduct
 
def listar (diccionario):
  for x in ProductosV:
    print(x,ProductosV[x])
    return ProductosV
"""
def Casos_descuentos(numProducto):
    reg_producto()
    if reg_producto().nproduct >=3 and reg_producto().nproduct<=4: 
       porcentaje5 = (reg_producto(ProductosV) * 5)/100
       print("Los productos aplican un descuento del 5'%'" , porcentaje5)
    elif reg_producto() >= 5 and reg_producto() <=6 :
        porcentaje10 = ((reg_producto(ProductosV) * 10)/100)
        print("el producto tiene 10'%'")
    elif reg_producto(): 
 """       
         
    

"""
def factura():
  info_usuario.name
  print(info_usuario.name)
  reg_producto()
  print(reg_producto)
  """


info_usuario()
reg_producto()
listar()
print(info_usuario)
print(reg_producto)
print(listar)
#print(Casos_descuentos)
#nombreprod , valorprod = reg_producto
"""

#1 
"""
num1 = int(input("Ingrese el primer numero : "))
num2 = int(input("Ingrese el segundo numero : "))

def sum_num(num1,num2):
    sum = num1 + num2
    print(f"La suma de los dos numeros es {sum}")
    return sum

sum_num(num1,num2)
"""
#2
"""
num1 = int(input("Ingrese el primer numero : "))

def cuadrado_numero(num1):
    c2 = num1 * num1
    print("El cuadrado de " , num1,"es", c2)
    return c2

cuadrado_numero(num1)
"""
#3
"""
lista1 = [1,93,23,2]

def listas_numeros(lista):
    sumlistas = sum(lista)
    print("La suma de las listas es " , sumlistas)
    return sumlistas

listas_numeros(lista1)
"""
#4
"""
listNum = [1,2,1,1,0,82]

def mayorNum(lista):
    mayor = 0 # se inicia la variable que almacenara el numero mayor
    for num in lista: #la variable num recorre cada numero de la lista
        if num > mayor:# validacion de cual es mayor
            mayor = num
            
    print("El numero mayor es : " , mayor)
    return mayor    
    
mayorNum(listNum)
"""
#5
"""

cadena = "Parangaricutirimícuaro"
cadena1 = "Parangaricutirimícuaro"

#Funcion con Metodo
def cadena_long(longitud):
    Clong = len(longitud)
    print(Clong)
    return Clong

cadena_long(cadena)

#Funcion sin Metodo
cadena1 = "Parangaricutirimícuaro"

def cadena_lng(long):
    cont = 0 # se inicia un contador para que almacene la cantidad de de caracteres
    for letra in long: # Recorra la cadena de caracteres 1 * 1 
        cont += 1 #Siempre que lo recorra lo cuenta y lo almacena
        
    print(cont)  
    return cont


cadena_lng(cadena1)
"""
#6
"""
listaP = [ 2, 4, 3, 6, 1, 8, 21, 37, 92]

def lista_Pares(lista):
    for num in lista: # for recorre la lista con una variable num
        if num  % 2 == 0: # la variable num una vez recorrido el dato, valida si es par o no
            print("Los numeros pares son :" , num)
    return num

lista_Pares(listaP)
"""

#7
"""
num1 = int(input("Ingrese el primer numero : "))
num2 = int(input("Ingrese el segundo numero : "))

def num_mayor(num1, num2):
    if num1 > num2: # validacion del numero mayor entre el primero y el segundo
        print("El numero mayor es : " , num1)
    else:  # si es diferente , el mayor es el segundo
        print("El numero mayor es : " , num2)
    return num1,num2

num_mayor(num1, num2)
"""

#8 
"""
lista_d = [9, 1, 7, 2, 0 , 13]

def lista_o(lista):
    print(lista) #se muestra la lista desordenada
    listaOrdenada = sorted(lista)# se muestra la lista ordenada
    print(listaOrdenada)
    return listaOrdenada

lista_o(lista_d)
"""
# Notas


# Strings: "" -> Funcionan como arrays, son iterables
#Todos los métodos de cadena devuelven nuevos valores. No modifican la cadena original.

texto = "hola"

len(texto) #Longitud
texto[0] #Valor de index específico
"h" in texto # O not in -> booleano
texto[0:1] #Slice, corta un pedacito, valor inicial - valor final
texto.upper() #Mayusculas
texto.lower() #Minusculas
texto.capitalize() #1 Mayuscula
texto.replace("","") #Reemplaza primer valor por el segundo
texto.split() #Separa las palabras si encuentra un separador. Ej "Hello" "World!, retorna lista"
texto.count("") #Numero de veces del parametro en el string
"".join(texto) #Une varios valores en un solo string, comillas el separador

# [:4] -> del inicio hasta index 4(no incluido)
# [1:] -> del index 1 al final
#[::] -> todo


# Listas [] -> arrays, orden determinado
#Para eliminar duplicados: mylist = list(dict.fromkeys(mylist)), otra opción es crear un [] nuevo recorriendo el anterior, si el valor no está ya, se agrega

lista = [1,2,3,4,5,6,7,8,9,10]
list(()) #Sirve para hacer una lista, usa doble parentesis
lista.append() #Añadir al final de la lista
lista.clear() #limpia la lista
lista.copy() #copia la lista
lista.extend("_lista") #se usa para unir dos listas
lista.sort() #ordena lista, no se puede asignar a otro valor, para esto mejor usar sorted(lista) que genera copia
lista.insert("index","valor") #Añade elemento en index especifico
lista.pop("index") #elimina segun index
lista.remove("valor") #elimina segun valor-> primer valor q encuentre
lista.reverse("reversa orden de lista")


#Tuplas () -> no cambian, solo se leen.

tupla = ("hola",) #Si es de solo 1 elemento, se pone la coma
tuple(()) #Sirve para hacer una tupla, usa doble parentesis

tupla.count()
tupla.index()


#Diccionarios = {"key":value}

diccionario = {"Nombre":"Bob","Edad":25,"Profesion": "Desarrollador"}

diccionario.get("key")	# Valor del key especificado
diccionario.items()	# Retorna lista que contiene tupla para cada par de key - value
#Ej:
for clase, valor in diccionario.items():
    print(f"""
    {clase} : {valor}
    """)
diccionario.keys() #Lista de keys
diccionario.pop("key") 	#Elimina elemento de la key
diccionario.popitem()	#Elimina el ultimo key-value insertado
diccionario.setdefault()	#Returns the value of the specified key. If the key does not exist: diccionario.key, with the specified value
diccionario.update({"key":"value"}) #Actualiza el diccionario con los nuevos key-value
diccionario.values() #Lista con todos los values


#Métodos de Python:
sum("iterable aqui")
min()
max()

salario = int(input("Ingresa tu salario: "))  #Solicitamos el salario del usuario
gastos = 0

categorias = {"alimentos": 0,  "transporte": 0, "vivienda": 0, "entretenimiento": 0, "otros": 0} #Categorías de los gastos

def recolectar_gastos(): #Recolectamos los gastos del usuario y actualizamos el diccionario
    while True:
      #Pedimos al usuario la categoría del gasto a ingresar
      print(
      """A continuación, ingresa tus gastos especificando una de las siguientes categorías:
      0. Para finalizar este menú
      - Alimentos
      - Transporte
      - Vivienda
      - Entretenimiento.
      """)
      categoria_ingresada = input().lower() #Ponemos en minusculas para facilitar la comparación con el diccionario

      if(categoria_ingresada == "0"): #Si escribe 0, se interrumpe el menú
        break
      elif categoria_ingresada not in categorias: #Si la categoría no se encuentra en el diccionario, el gasto a ingresar pasa a formar parte de otros
        monto = int(input("Ingresa el valor del gasto: "))
        categorias["otros"] += monto
      else:
        monto = int(input("Ingresa el valor del gasto: "))#Si la categoría está en el diccionario, actualizamos el value con el monto ingresado
        categorias[categoria_ingresada] += monto
      print(categorias)

def calcular_gastos(_categorias): #Sumamos los valores de las diferentes categorías de gastos y lo retornamos para usarlo en otra funcion
  gastos = sum(_categorias.values())
  return gastos

def salario_restante(): #Calculamos e imprimimos el salario restante según los gastos calculados anteriormente
  total = salario - calcular_gastos(categorias) #Salario - gastos (esto retorna la función)
  #Imprimimos el saldo restante, y el gasto total
  print(f"Estás gastando {total} más de lo que ganas")  if total < 0 else print(f"El saldo restante es {total}, gastaste {calcular_gastos(categorias)}")

def mostrar_gastos(_categorias): #Mostramos los gastos categorizados
  for categoria, valor in _categorias.items():
    print(f"""
    En la {categoria} gastaste {valor}
    """)

#Ejecutamos las funciones.
recolectar_gastos()
calcular_gastos(categorias)
salario_restante()
mostrar_gastos(categorias)
