# Cats Coding
Das hier ist ein kleines Python-Projekt von mir, bei dem jeden Tag ein cartoonartiges Katzenbild generiert und auf Instagram unter dem Account "[cats_coding](https://www.instagram.com/cats_coding/)" hochgeladen wird.

## Technische Umsetzung
Als erstes sucht das Programm zufällig eine Katze als Basis aus dem Ordner "[cat_templates](https://github.com/hydracode77/cats_coding/tree/main/cat_templates)" aus. 
Dann wird noch Zubehör, auch zufällig, aus dem Ordner "[accessories](https://github.com/hydracode77/cats_coding/tree/main/accessories)" ausgewählt und an der richtigen Stelle angefügt.
Die Katze wird jetzt vor einen weißen Hintergrund gesetzt, das Bild wird ins richtige Verhältnis gebracht, zu .jpeg konvertiert und gespeichert.
Anschließend wird es mit der caption "Wieder mal ein schönes Bild, oder?" hochgeladen.
Dieser Vorgang wird dann nach 24h wiederholt.

# Kontinuität
Damit das Programm auch tagelang durchlaufen kann, habe ich es auf meinen Raspberry Pi 4 kopiert und dort gestartet. 
Sollte beim Konvertieren oder beim Hochladen des Bildes ein Fehler auftreten, bekomme ich mithilfe der Bibilothek `pushbullet` eine Benachichtigung auf mein Smartphone.

## Instagram - cats_coding
[<img src="https://i.postimg.cc/wMQrFzvy/cats.png" alt="cats_coding_insta" width="380" height="360">](https://www.instagram.com/cats_coding/)

## Update, 5. März 2024:
Durch technische Probleme (welche wahrscheinlich dem zugrunde liegen, dass Instagram solche Bots nicht besonders mag) ist das Projekt temporär inaktiv, solange das Problem noch besteht. (:
