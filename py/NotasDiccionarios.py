# un diccionario es una estructura de datos que permite almacenar pares clave-valor.



mi_diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

# Acceder a un valor utilizando una clave
print(mi_diccionario['nombre'])  # Output: Juan

# Agregar una nueva clave-valor
mi_diccionario['ocupacion'] = 'Ingeniero'

# Modificar un valor existente
mi_diccionario['edad'] = 31

# Eliminar una clave-valor
del mi_diccionario['ciudad']

print(mi_diccionario)  # Output: {'nombre': 'Juan', 'edad': 31, 'ocupacion': 'Ingeniero'}



""" Metodos de los diccionarios"""

# dict.values(): Devuelve una vista de los valores del diccionario. IMPORTANTE

# dict.items(): Devuelve una vista de los pares clave-valor del diccionario. IMPORTANTE

# dict.keys(): Devuelve una vista de las claves del diccionario.

# dict.clear(): Elimina todos los elementos del diccionario.

# len(dict): Devuelve la cantidad de elementos (pares clave-valor) en el diccionario.

#2f : si se tiene un dato tipo float es igual a 2.14 A 2

#.capitalize() : Primer caracter en mayus



# Devolver la lista de valores de un diccionario """

mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
valores = mi_diccionario.values()
print(valores)  # Output: dict_values([1, 2, 3])




""" Devuelve clave-valor en el diccionario.  """

mi_diccionario = {'a': 1, 'b': 2, 'c': 3}
items = mi_diccionario.items()
print(items)
"""



""" Iterar sobre los valores """
"""
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

print("Iterando sobre los valores del diccionario:")
for valor in mi_diccionario.values():
    print(valor)
"""


""" Iterar sobre los pares clave-valor """


"""
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

# Iterar sobre los pares clave-valor
print("Iterando sobre los pares clave-valor del diccionario:")
for clave, valor in mi_diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")
"""


""" Iterar sobre las claves """


"""
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

# Obtener una vista de las claves del diccionario
claves = mi_diccionario.keys()

# Iterar sobre las claves y mostrarlas
print("Claves del diccionario:")
for clave in claves:
    print(clave)
"""


""" Eliminar todoos los elementos del diccionario """

mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

# Limpiar el diccionario
mi_diccionario.clear()

# Verificar si el diccionario está vacío
if not mi_diccionario:
    print("El diccionario está vacío.")
else:
    print("El diccionario no está vacío.")




""" Ejemplos de posibles usos de .values() y .items() en un caso real """


def calcular_saldo_restante(salario, gastos):
    total_gastos = sum(gastos.values())
    saldo_restante = salario - total_gastos
    return saldo_restante

def mostrar_resumen_gastos(gastos, saldo_restante):
    print("\nResumen de gastos:")
    for categoria, monto in gastos.items():
        print(f"{categoria.capitalize()}: ${monto:.2f}")
    print(f"\nSaldo restante: ${saldo_restante:.2f}")




# .2f formatea un numero tipo float a dos decimales
# ejemplo
numero = 3.14159
cadena_formateada = "{:.2f}".format(numero)
print(cadena_formateada)  # Salida: 3.14


#Problemas de diccionario




# Problema 1: calcular la suma de valores de un diccionario


def calcular_suma(diccionario):
    suma_resultado = {}
    for clave, valores in diccionario.items():
        suma_resultado[clave] = sum(valores)
    return suma_resultado

# Ejemplo de uso
mi_diccionario = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
resultado = calcular_suma(mi_diccionario)
print(resultado)




# Problema 2: Contar la cantidad de veces que aparece cada letra en una cadena
# y la salida mostrarla en formato de diccionario

def contar_letras(cadena):
    frecuencia_letras = {}
    for letra in cadena:
        if letra in frecuencia_letras:
            frecuencia_letras[letra] += 1
        else:
            frecuencia_letras[letra] = 1
    return frecuencia_letras

# Ejemplo de uso
cadena = "hola mundo"
frecuencia = contar_letras(cadena)
print(frecuencia)


# Problema 3: Calcular la cantidad de veces que aparece cada numero en una lista
# y la salida mostrarla en formato de diccionario

def contar_numeros(lista):
    frecuencia_numeros = {}
    for numero in lista:
        if numero in frecuencia_numeros:
            frecuencia_numeros[numero] += 1
        else:
            frecuencia_numeros[numero] = 1
    return frecuencia_numeros

# Ejemplo de uso
numeros = [1, 2, 3, 2, 3, 3, 4, 4, 4, 4]
frecuencia = contar_numeros(numeros)
print(frecuencia)


