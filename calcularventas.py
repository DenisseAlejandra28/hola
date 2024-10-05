# Definir una función para leer el archivo y procesar las ventas
def leer_ventas(archivo):
    ventas = []
    
    # Abrir el archivo en modo lectura
    with open(archivo, 'r') as f:
        for linea in f:
            # Separar los valores por comas y convertirlos a enteros
            datos_tienda = list(map(int, linea.strip().split(',')))
            ventas.append(datos_tienda)
    
    return ventas

# Definir una función para calcular y mostrar el total de ventas
def mostrar_totales(ventas):
    for i, tienda in enumerate(ventas):
        total = sum(tienda)  # Calcular el total de ventas de la tienda
        print(f'Total de ventas de la tienda {i + 1}: {total}')

# Nombre del archivo a leer
archivo_ventas = 'ventas.txt'

# Leer las ventas del archivo
ventas = leer_ventas(archivo_ventas)

# Mostrar los totales de ventas
mostrar_totales(ventas)


