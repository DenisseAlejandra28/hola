# solicitar ingreso del lado del cuadrado al usuario
lado = float(input("ingrese el lado del cuadrado: "))
# calcular el area del cuadrado
area = lado ** 2
# calcular el area del triangulo equilatero
area_triangulo = ((3 ** (0.5))/4)* (lado ** 2)
# mostrar el resultado
print(f"El area del cuadrado es: {area:.2f}")
print(f"El area del triangulo es: {area_triangulo:.2f}")