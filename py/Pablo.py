"""
pregunta = input("Escriba su nombre : ")
cedula = int(input("Escriba su numero de cedula : "))
print("Su nombre es: ", pregunta,"Y su cedula es", cedula)
"""
"""
edad = int(input("Escriba su edad para verficiar si su edad esta en el rango de edad elegible."))

if edad >= 18 and edad <=65:
    print("Eres elegible")
else:
    print("No eres elegible")

"""
"""
userv = "usuario123"
passwordv = "contraseña456"

""""""
i = 0
j = 0
"""
while i < 3:
    user = input("Ingrese su Nombre de Usuario por favor : ")
    password = input("Ingrese su contraseña : ")
    
    if user == userv and password == passwordv :
        print("Inicio de sesion exitoso")
        i = i + 3
     
    elif password != passwordv:
        print("Contraseña o Usuario incorrecto, Verifique su usuario o contraseña.")
        
        j += 1
        i += 1
    if j== 3: 
        print("Acabaste tu numero de intentos")


    


salario = int(input("Ingresa tu salario: "))  #Solicitamos el salario del usuario
gastos = 0

categorias = {"alimentos": 0, "transporte": 0, "vivienda": 0, "entretenimiento": 0, "otros": 0} #Categorías de los gastos

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
    
""""
if i == 3: 
    print("Acabaste tu numero de intentos")

    """

