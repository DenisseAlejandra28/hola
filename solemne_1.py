precio = int(input("ingrese el precio:"))
pago = int(input("ingrese el monto de pago:"))

vuelto = pago - precio

billete_20000 = int(vuelto / 20000)
vuelto =vuelto - billete_20000 * 20000
print(billete_20000, "billetes de $20000")

billete_10000 = int(vuelto / 10000)
vuelto = vuelto % 10000
print(billete_10000, "billetes de 10.000")

billete_5000 = int(vuelto / 5000)
vuelto = vuelto % 10000
print(billete_10000, "billetes de 10.000")
print(bienvenido)