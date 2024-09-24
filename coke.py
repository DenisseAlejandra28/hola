# Solicitar al usuario que inserte una moneda

moneda = int(input("ingrese una moneda de 25, 10 o 5 centavos: "))
monedas_aceptadas = [25, 10, 5]
saldo = 50
while saldo > 0:
    print(f"monto saldo: {saldo} centavos")
    moneda = int(input("ingrese una moneda de 25, 10 o 5 centavos: "))
# preguntar si la moneda es la aceptada
if moneda in monedas_aceptadas:
    saldo = saldo - moneda
else:
    print("insertar solo monedas de 25, 10 o 5 centavos. ")    
if saldo < 0:
    print(f"su vuelto es: {saldo} centavos") 
else:
    print("Gracias!")  

# si moneda es ok, restar 50 - moneda