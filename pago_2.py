# solicitar ingreso al usuario
precio = int(input("ingrese el precio: "))
monto_pago = int(input("ingrese el pago: "))

# realizar calculos
vuelto = monto_pago - precio

# calcular cuantos billetes de a $ 1.000 se requieren

billetes_1000 = int(vuelto / 1000)
print(billetes_1000)

# mostrar el resultado
print(f"el vuelto es {vuelto}")