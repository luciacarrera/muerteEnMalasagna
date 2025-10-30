import random

repeated_actions = [
    "Deciros el nombre y un dato random sobre vosotros",
    "Comentad vuestra red flag, beige flag y green flag",
    "Elegid por votación el disfraz más currado/chulo (dentro y fuera del equipo) y apuntadlo en un papel",
    "Cread un disfraz nuevo con lo que encontréis (foto)",
    "Cread una poción en un vaso(vuestra bebida)  y elegid; 1.Uno del equipo la bebe entera. 2.Todos bebéis un poco",
    "Discutid sobre que monstruo serías cada uno y apuntadlo en un papel",
    "Foto con alguien vestido como la mascota de vuestro equipo",
    "Cread un disfraz nuevo con lo que encontréis (foto)",
    "Grabad como asustáis a alguien de otro equipo",
]

northern_bars = [
    "Bar Taberna los claveles",
    "Tiki Volcano Bar",
    "Café de Ruiz",
    "Barroco el bar de Uadibloc",
    "Aleatorio Bar",
]
southern_bars = [
    "SAMBHAD the cocktail bar",
    "Bar Menuda History",
    "El Rincón de La Habana",
    "Loreto Coffee Bar",
    "Santamaría Coctelería",
    "Pub Prada",
    "La Prensa Burgers & Beers",
]

bars = [
    "Bar Antonio",
    "La Pasa Gin Bar",
    "Ca Angelita - Bar Conde Duque",
    "El Amor Hermoso Bar",
    "Bravo Wine Bar",
    "La Doña",
    "Marrufo Coctelería",
    "J&J's Books and Coffee",
    "Los más Canallas de Malasaña",
    "El Pez Gato",
    "1862 Dry Bar",
    "Sidrería La Cuenca",
    "Chin Chin",
    "Medium Club",
    "Picnic",
    "Esoterica Speakeasy",
    "Rockade Malasaña",
    "Estación Malasaña",
    "Malasaña Sports Pub",
    "Casa Julio",
    "Maniquí Bar",
    "Lolita Vintage Café",
    "Infernales Café Bar",
    "Coco Bar - Pastrami",
    "Casa Macareno",
    "Freeway",
    "Casa Camacho",
    "The Toast Taproom",
    "El Rincón",
    "Estar Café",
    "Hotel California",
    "Rebelde Malasaña",
    "Maria Puñales",
    "Calandría Bar",
    "Cervecería El Metro de Manuela Malasaña",
    "Café Pepe Botella",
    "El 2D",
]

tiktoks = [
    "chasquidos familia adams",
    "trend the sugar on my tongue ",
    "trend Ramalama (bang bang)",
    "trend no responde pero siempre tira un liky",
    "trend where the hell is my  husband",
    "frases rajoy",
    "trend if you want it, take it, I should’ve said it before",
]


easy_search = [
    "hombre lobo",
    "zombie",
    "demonio",
    "fantasma",
    "pirata",
    "monja",
]

hard_search = [
    "Miércoles Addams",
    "El Joker",
    "Cruella de Vil",
    "Harley Quinn",
    "Maléfica",
    "Jason Viernes 13",
    "Chuky",
    "Freddy Krueger",
]

with open("output.txt", "w", encoding="utf-8") as f:
    for team in range(5):
        f.write("---- BARBINGO EQUIPO " + str(team + 1) + " ----\n")
        # bar 1
        chosenBarId = random.randrange(len(bars))
        chosen_bar = bars.pop(chosenBarId)
        f.write("Ronda en " + chosen_bar + "\n")

        # bar 2
        chosenBarId = random.randrange(len(bars))
        chosen_bar = bars.pop(chosenBarId)
        f.write("Ronda de chupitos en " + chosen_bar + "\n")

        # bar 3
        chosenBarId = random.randrange(len(northern_bars))
        chosen_bar = northern_bars.pop(chosenBarId)
        f.write("Ronda en " + chosen_bar + "\n")

        # bar 4
        chosenBarId = random.randrange(len(southern_bars))
        chosen_bar = southern_bars.pop(chosenBarId)
        f.write("Ronda en " + chosen_bar + "\n")

        # print actions
        for action in repeated_actions:
            f.write(action + "\n")

        # tiktok
        chosenTiktokId = random.randrange(len(tiktoks))
        chosen_tiktok = tiktoks.pop(chosenTiktokId)
        f.write("Haced un tiktok con: " + chosen_tiktok + "\n")

        # search easy
        chosenSearchId = random.randrange(len(easy_search))
        chosen_search = easy_search.pop(chosenSearchId)
        f.write("Encontrar y haceros una foto con un" + chosen_search + "\n")

        # search hard
        chosenSearchId = random.randrange(len(hard_search))
        chosen_search = hard_search.pop(chosenSearchId)
        f.write("Encontrar y haceros una foto con " + chosen_search + "\n")

        f.write("\n")
