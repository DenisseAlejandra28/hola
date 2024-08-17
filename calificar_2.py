puntaje = int(input("ingresar puntos del 1 al 100: "))

if 90 <= puntaje <= 100:
    print("calificacion: A")
elif 80 <= puntaje <= 90:
    print("calificacion: B")
elif 70 <= puntaje <= 80:
    print("calificacion: C")
elif 60 <= puntaje <= 70:
    print("calificacion: D")
else:
    print("calificacion: F")