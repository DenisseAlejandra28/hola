input("¡bienvenido!")
L = float(input("ingrese el lado de un poligono regular: "))

area_triangulo = ((3)**(0.5))*(L ** 2)/4
area_cuadrado = L ** 2
area_pentagono = (L ** 2) * (25 + 10 *(5 ** 0.5)) ** 0.5 / 4

print(f"area del pentagono regular: {area_pentagono:.2f}")
print(f"area del triangulo equilatero de lado: {area_triangulo:.2f}")
print(f"area del cuadrado de lado: {area_cuadrado:.2f}")
