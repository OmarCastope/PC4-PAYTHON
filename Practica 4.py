
# Problema 1: 
# Tienes un fichero temperaturas.txt que contiene registros de temperaturas diarias en formato 
# CSV. Cada línea del fichero tiene la siguiente estructura: fecha,temperatura. Debes leer el 
# fichero, calcular la temperatura promedio, la temperatura máxima y la mínima. Finalmente, 
# debes escribir los resultados en un nuevo fichero resumen_temperaturas.txt. 

def procesar_temperaturas(archivo_entrada, archivo_salida):
    temperaturas = []

    with open(archivo_entrada, 'r') as f:
        for linea in f:
            try:
                fecha, temp = linea.strip().split(',')
                temperatura = float(temp)
                temperaturas.append(temperatura)
            except ValueError:
                print(f"Línea inválida: {linea.strip()}")

    if not temperaturas:
        print("No se encontraron temperaturas válidas.")
        return

    promedio = sum(temperaturas) / len(temperaturas)
    maxima = max(temperaturas)
    minima = min(temperaturas)

    with open(archivo_salida, 'w') as f:
        f.write(f"Temperatura promedio: {promedio:.2f}°C\n")
        f.write(f"Temperatura máxima: {maxima:.2f}°C\n")
        f.write(f"Temperatura mínima: {minima:.2f}°C\n")

    print(f"Resumen guardado en '{archivo_salida}'.")


entrada = "temperaturas.txt"
salida = "resumen_temperaturas.txt"

procesar_temperaturas(entrada, salida)


#Problema 2: 
#Escriba un programa que realice las siguientes tareas (Puede usar clases y/o funciones, 
#también puede usar un menú para organizar su programa): - 
#Solicite un número entero entre 1 y 10 y guarde en un fichero con el nombre 
#tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido. - - 
#Notas: - - - 
#Solicite un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de 
#multiplicar de ese número, donde “n” es el número introducido, y la muestre por 
#pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de 
#ello. 
#Solicite dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de 
#multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero 
#no existe debe mostrar un mensaje por pantalla informando de ello. 

import os

def generar_tabla(n):
    nombre_archivo = f"tabla-{n}.txt"
    with open(nombre_archivo, 'w') as f:
        for i in range(1, 11):
            f.write(f"{n} x {i} = {n*i}\n")
    print(f"Tabla del {n} guardada en {nombre_archivo}.")

def leer_tabla(n):
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, 'r') as f:
            contenido = f.read()
            print(f"\nContenido de {nombre_archivo}:\n{contenido}")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

def leer_linea_tabla(n, m):
    nombre_archivo = f"tabla-{n}.txt"
    try:
        with open(nombre_archivo, 'r') as f:
            lineas = f.readlines()
            if 1 <= m <= len(lineas):
                print(f"Línea {m}: {lineas[m-1].strip()}")
            else:
                print(f"El archivo no tiene una línea {m}.")
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")

def solicitar_numero(mensaje):
    while True:
        try:
            num = int(input(mensaje))
            if 1 <= num <= 10:
                return num
            else:
                print("Por favor, introduce un número entre 1 y 10.")
        except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")

def menu():
    while True:
        print("\nMENÚ:")
        print("1. Generar tabla de multiplicar y guardar en archivo")
        print("2. Leer y mostrar tabla de multiplicar desde archivo")
        print("3. Leer línea específica de una tabla")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            n = solicitar_numero("Ingrese un número entre 1 y 10: ")
            generar_tabla(n)
        elif opcion == "2":
            n = solicitar_numero("Ingrese un número entre 1 y 10: ")
            leer_tabla(n)
        elif opcion == "3":
            n = solicitar_numero("Ingrese el número de la tabla (1-10): ")
            m = solicitar_numero("Ingrese el número de la línea (1-10): ")
            leer_linea_tabla(n, m)
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()

#Problema 3: 
#Una forma de medir la complejidad de un programa es contar su número de líneas de código 
#(LOC), excluyendo las líneas en blanco y los comentarios. Por ejemplo, un programa como 
#Del código se observa que este solo tiene dos líneas de código, no cuatro, ya que su primera 
#línea es un comentario y su segunda línea está en blanco (es decir, solo espacios en blanco). 
#Esto no es tanto, por lo que es probable que el programa no sea tan complejo. 
#Implemente un programa donde se le solicitará al usuario la ruta de un archivo .py (nombre y 
#ruta). Y retorne la cantidad de líneas de código de ese archivo, excluyendo los comentarios y 
#líneas en blanco. Si el usuario ingresa una ruta inválida o si el nombre del archivo no termina en 
#py, su programa no retornará ningún resultado.  

import os

def contar_lineas_codigo(ruta_archivo):
    if not ruta_archivo.endswith(".py"):
        print("El archivo debe tener extensión .py.")
        return

    if not os.path.isfile(ruta_archivo):
        print("La ruta del archivo no es válida.")
        return

    lineas_codigo = 0
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if linea_limpia and not linea_limpia.startswith('#'):
                    lineas_codigo += 1
        print(f"Líneas de código (excluyendo comentarios y líneas en blanco): {lineas_codigo}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

# Ejecutar el programa
ruta = input("Ingrese la ruta del archivo .py: ").strip()
contar_lineas_codigo(ruta)