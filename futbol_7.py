jugadores = [
    {"nombre": "Vidal", "equipo": "colo colo","representante": "Fernando Felicevich"},
    {"nombre": "Palacios", "equipo": "colo colo","representante": ""},
    {"nombre": "Falcon", "equipo": "colo colo","representante": "Gerardo Arias"},
    {"nombre": "Charles Aranguiz", "equipo": "Universidad de Chile","representante": "Andres Cury"}
]
for jugador in  jugadores:
    print(jugador["nombre"], jugador["equipo"], jugador["representante"],sep=" - ")
