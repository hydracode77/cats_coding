from PIL import Image
from random import choice
import time
from instabot import Bot
import shutil
import os
from pushbullet import Pushbullet
API_KEY = "API_KEY"
push_notification = Pushbullet(API_KEY)


bot = Bot()  # Bot initialisieren
bot.login(username="cats_coding", password="password") # anmelden

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

def convert_image(input_path, output_path): # Bild von png zu jpeg umwandeln, weil insta kein png mag
    img = Image.open(input_path)

    img_with_white_background = Image.new("RGB", (1026, 1026), "white")  # weißer hintergrund, welcher bissl größer ist als normales Bild
    img_with_white_background.paste(img, (161, 46), mask=img.split()[3])  # Bild auf den Hintergrund in die Mitte platzieren, alphakanal verwenden

    img_with_white_background.save(output_path, "JPEG") # bild als jpeg speichern


while True:
    try: shutil.rmtree("config"); print("Ordner config gelöscht")  # erstmal config vom letzten Uploaden löschen (sonst error)
    except: pass
    try: os.remove("result/katze_bild_converted.jpeg.REMOVE_ME"); print("katze_bild2.jpeg.REMOVE_ME gelöscht") # genauso auch das ding
    except: pass

    cat_template = choice(Cats.list) # eine Katze zufällig aussuchen
    cat = cat_template.copy()  # Kopie verwenden, damit es nicht für nachfolgende Iterationen verändert wird
    glass_acc = choice(Accesories.eyes_list)  # eine Brille zuällig aussuchen
    chain_acc = choice(Accesories.medal_list) # eine Medallie zufällig aussuchen
    hat_acc = choice(Accesories.hat_list) # eine Kopfbedeckung zufällig aussuchen

    # Accesories an richtiger Stelle auf Katze-bild platzieren
    # Glasses
    if not glass_acc is None:
        if glass_acc == Accesories.eyes_list[0]:  # sunglasses
            cat.paste(glass_acc, (83, 362), glass_acc)
        elif glass_acc == Accesories.eyes_list[1]:  # monocle
            cat.paste(glass_acc, (316, 361), glass_acc)
        elif glass_acc == Accesories.eyes_list[2]:  # eye patch
            cat.paste(glass_acc, (189, 226), glass_acc)
        elif glass_acc == Accesories.eyes_list[3]:  # ski googles
            cat.paste(glass_acc, (84, 309), glass_acc)

    # Medallien
    if not chain_acc is None:
        cat.paste(chain_acc, (272, 609), chain_acc)

    # Kopfbedeckungen
    if not hat_acc is None:
        if hat_acc == Accesories.hat_list[0]:  # zylinder
            cat.paste(hat_acc, (130, 0), hat_acc)
        elif hat_acc == Accesories.hat_list[1]:  # cowboy
            cat.paste(hat_acc, (31, 17), hat_acc)
        elif hat_acc == Accesories.hat_list[2]: # crown
            cat.paste(hat_acc, (84, 27), hat_acc)
        elif hat_acc == Accesories.hat_list[3]: # police hat
            cat.paste(hat_acc, (129, 61), hat_acc)

    try:
        cat.save(f"result/katze_bild.png", format="PNG") # Bild exportieren
        convert_image("result/katze_bild.png", "result/katze_bild_converted.jpeg") # Bild von jpeg zu png konvertieren mit white background
    except:
        push_notification.push_note("Fehler - save & convert", "Bei dem Insta-Bot Projekt gibt es ein Fehler im Bereich speichern und konvertieren des generierten Bildes.")

    # Auf Insta hochladen
    try:
        bot.upload_photo("result/katze_bild_converted.jpeg", caption="Wieder mal ein schönes Bild, oder?")
    except:
        push_notification.push_note("Fehler - Upload", "Bei dem Insta-Bot Projekt gibt es ein Fehler beim Hochladen des Bildes.")

    # nach upload 24h warten
    time.sleep(86400) # = 24 Stunden
