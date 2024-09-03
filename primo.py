n = int(input("ingrese numero entero: "))

for i in range(2, n):
    if n % i == 0:
       es_primo = False
    else:
        es_primo = True

if es_primo:
     print(f"{n} no es numero primo ")
else:
     print(f"{n} es numero primo")