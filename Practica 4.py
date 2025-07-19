
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


