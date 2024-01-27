from PIL import Image
from random import choice
import time

number_of_images = 10  # wie viele Images generiert werden sollen


class Accesories:
    sunglasses = Image.open("accessories/sunglasses.png").convert("RGBA")
    monocle = Image.open("accessories/monocle.png").convert("RGBA")
    eye_patch = Image.open("accessories/augenklappe.png").convert("RGBA")
    ski_googles = Image.open("accessories/ski_googles.png").convert("RGBA")

    silver_medal = Image.open("accessories/silver_medal.png").convert("RGBA")
    gold_medal = Image.open("accessories/gold_medal.png").convert("RGBA")
    bronze_medal = Image.open("accessories/bronze_medal.png").convert("RGBA")

    zylinder = Image.open("accessories/zylinder.png").convert("RGBA")
    cowboy_hat = Image.open("accessories/cowboy_hat.png").convert("RGBA")
    crown = Image.open("accessories/crown.png").convert("RGBA")
    police_hat = Image.open("accessories/police_hat.png").convert("RGBA")
    # astronout_helmet = Image.open("accessories/astronout_helmet.png").convert("RGBA")

    eyes_list = [sunglasses, monocle, eye_patch, ski_googles, None]  # alle Accessoires auf Augenhöhe
    medal_list = [bronze_medal, silver_medal, gold_medal, None]  # alle am Chain, auch None damit Standard auch geht
    hat_list = [zylinder, cowboy_hat, crown, police_hat, None]


class Cats:
    black = Image.open("cat_templates/black.png").convert("RGBA")
    grey_brown = Image.open("cat_templates/grey_brown.png").convert("RGBA")
    orange = Image.open("cat_templates/orange.png").convert("RGBA")
    purple = Image.open("cat_templates/purple.png").convert("RGBA")
    white = Image.open("cat_templates/white.png").convert("RGBA")
    yellow = Image.open("cat_templates/yellow.png").convert("RGBA")
    list = [black, grey_brown, orange, purple, white, yellow]


# for i in range(0, number_of_images):
while True:
    cat_template = choice(Cats.list)  # damit bild nicht für nachfolgende Iterationen verändert wird
    cat = cat_template.copy()  # dann eben nur copy verwenden
    glass_acc = choice(Accesories.eyes_list)
    chain_acc = choice(Accesories.medal_list)
    hat_acc = choice(Accesories.hat_list)

    # Überlagerung der Bilder
    if not glass_acc is None:
        if glass_acc == Accesories.eyes_list[0]:  # sunglasses
            cat.paste(glass_acc, (83, 362), glass_acc)
        elif glass_acc == Accesories.eyes_list[1]:  # monocle
            cat.paste(glass_acc, (316, 361), glass_acc)
        elif glass_acc == Accesories.eyes_list[2]:  # eye patch
            cat.paste(glass_acc, (189, 226), glass_acc)
        elif glass_acc == Accesories.eyes_list[3]:  # ski googles
            cat.paste(glass_acc, (84, 309), glass_acc)

    if not chain_acc is None:
        cat.paste(chain_acc, (272, 609), chain_acc)

    if not hat_acc is None:
        if hat_acc == Accesories.hat_list[0]:  # zylinder
            cat.paste(hat_acc, (130, 0), hat_acc)
        elif hat_acc == Accesories.hat_list[1]:  # cowboy
            cat.paste(hat_acc, (31, 17), hat_acc)
        elif hat_acc == Accesories.hat_list[2]: # crown
            cat.paste(hat_acc, (84, 27), hat_acc)
        elif hat_acc == Accesories.hat_list[3]: # police hat
            cat.paste(hat_acc, (129, 61), hat_acc)

    # Bild exportieren
    cat.save(f"result/katze_bild{i}.png", format="PNG")
