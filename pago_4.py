# solicitar ingreso al usuario
precio = int(input("ingrese el precio: "))
monto_pago = int(input("ingrese el pago: "))
# realizar calculos
vuelto = monto_pago - precio
# calcular cuantos billetes de a $ 1.000 se requieren
billetes_1000 = int(vuelto / 1000)
vuelto = vuelto - (billetes_1000 * 1000) # vuelto % 1000

# calcular monedas de a $ 500 se requieren
monedas_500 = int( vuelto / 500)
vuelto = vuelto % 500
# calcular monedas de a $ 100 se requieren
monedas_100 = int(vuelto / 100)
# mostrar el resultado
print(f"- {billetes_1000} billetes de $1.000")
print(f"- {monedas_500} monedas de $500")
print(f"- {monedas_100} monedas de $100")
