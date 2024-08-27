precios = {
    "cafe": 1500,
    "te": 1000,
    "jugo natural": 2000,
    "pastel de chocolate": 2500,
    "tarta de frutas": 3000,
}
pedidos = {
  "cafe": int(input("ingrese la cantidad de cafe: ")),
    "te": int(input("ingrese la cantidad de te: ")),
    "jugo natural": int(input("ingrese la cantidad de jugo: ")),
    "pastel de chocolate": int(input("ingrese la cantidad de chocolate: ")),
    "tarta de frutas": int(input("ingrese la cantidad de frutas: ")), 
}
total = 0
for producto, cantidad in pedidos.items():
   total += cantidad * precios[producto]
print(total)