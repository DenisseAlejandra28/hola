#verificar si un numero es multiplo de otro
m = int(input("ingrese el primer numero: "))
n = int(input("ingrese el segundo numero: "))
resto = m % n

if resto == 0:
    print(f"{m} es multiplo de {n}")
else:
    print(f"{m} no es multiplo de {n}")