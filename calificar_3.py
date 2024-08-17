puntaje = int(input("ingresar puntos del 1 al 100: "))

if puntaje >= 90:
    print("calificacion: A")
elif puntaje >= 80:
    print("calificacion: B")
elif puntaje >= 70:
    print("calificacion: C")
elif puntaje >= 60:
    print("calificacion: D")
else:
    print("calificacion: F")