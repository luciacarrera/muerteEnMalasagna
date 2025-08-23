import random

bars = [
    "Hotel California",
    "La Manuela",
    "Ocean Rock Bar",
    "Poca Verguenza",
    # "Red Bar",
    # "Dekada",
    # "Cervecería El Metro de Manuela Malasaña",
    "María Puñales",
    "Madrid Me Mata",
    "El Penta",
    "Tupper Ware",
    "Estar Café",
    "Wall St",
    "Freeway",
    "Super pop bar",
    "Mongo bar",
]

teams = ["un fantasma", "una bruja", "un diablillo", "una payasa"]

single_actions = [
    "CHUPITO!",
    "COPAZO!",
    "Grita Hola Malasaña!",
    "Selfie con la people",
    "Foto del panorama",
    "Consigue el instagram de alguien",
    "Consigue un autógrafo",
    "Baila la Macarena",
    "Canta el cumpleaños feliz",
    "Haz el Siu como Ronaldo",
    "Imita a Rajoy",
    "Di un Trabalenguas 3 veces seguidas",
    "Haz el Michael Jackson",
    "Baila como Trump",
    "Quitate un zapato",
    "Canta la cancion de apertura de una serie",
    "Selfie con morritos",
    "Habla todo el rato con acento argentino",
    "Habla todo el rato en inglés",
    "Hidalgo de tu cerve/tinto",
    "Conviertete en una pija o una choni",
    "Hazte pasar por un famoso",
    "Solo puedes decir que si",
    "Pide un aperitivo y compartelo",
]

group_actions = [
    "Presentate a",
    "Preguntale que rasgo tienen de su signo a",
    "Cuentale un chiste a",
    "Preguntale sobre su último viaje a",
    "Que te cuente un chiste de humor negro",
    "Preguntale cual es su sueño a",
    "Preguntale tu anécdota más vergonzosa a",
    "Preguntale cual es su imperio romano a",
    "Enseñale tu meme favorito a",
    "Cuentale un secreto a",
    "Explica quien es tu celebrity crush a",
    "Explica porque Miley o Selena es mejor a",
    "Debate sobre la mejor pelí de animación con",
]

with open("output.txt", "w", encoding="utf-8") as f:
    for bar in range(1, len(bars) + 1):
        for action in single_actions:
            f.write(f"Bar #{bar} - {action}\n")

        for group_action in range(1, len(group_actions) + 1):
            team1 = random.choice(teams)
            f.write(f"Bar #{bar} - Interacción Social #{group_action} con un {team1}\n")

            teams_left = teams_left = [t for t in teams if t != team1]
            team2 = random.choice(teams_left)
            f.write(f"Bar #{bar} - Interacción Social #{group_action} con un {team2}\n")


for bar in bars:
    bar_num = bars.index(bar) + 1
    if bar_num < 10:
        bar_num = f"0{bar_num}"
    print(f"#{bar_num}:".ljust(4), bar)
print()
for interaccion in group_actions:
    num = group_actions.index(interaccion) + 1
    if num < 10:
        num = f"0{num}"
    print(f"#{num}:".ljust(4), interaccion, "X")
