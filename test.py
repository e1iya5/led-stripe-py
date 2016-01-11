"""
test.py

Ein kleines Test-Programm für die kleine LED-Stripe-Library.
Wenn alles glatt läuft, müsste die Lichterkette von rot über lila bis blau erleuchten.

© Elias Gürlich, 2016
"""

from lib import LED_Stripe, LED_Stripe_Datagram, LED # Alles aus der LED-Stripe-Lib importieren
import math # Importiere natives Math-Modul

HOST_NAME = "localhost"
PORT = 2342

led_stripe = LED_Stripe(HOST_NAME, PORT) # Erzeuge Lichterkette mit diesem Host und Port

leds = [] # Hier kommen die LEDs rein *-*
for i in range(0, 103): # Mache 103 mal...
    led = LED(0xff, 0x00, math.ceil(0x00 + (0xff/103) * i)) # Fange bei ganz rot an und werde immer lilaner
    leds.append(led) # Füge LED hinzu

for i in range(0, 103): # Mache nochmal 103 mal...
    led = LED(math.ceil(0xff - (0xff/103) * i), 0x00, 0xff) # Fange bei ganz lila an und werde immer blauer
    leds.append(led) # Füge LED hinzu

datagram = LED_Stripe_Datagram(priority=0xff, command=0x00, leds=leds) # Erzeuge Datagram mit Priorität 255, (seeeeehr hoch) Kommando 0 (Setze LED-Farben) und den ganzen LEDs, die wir definiert haben

led_stripe.send(datagram) # Sende Datagram an Lichterkette

# Wenn alles glatt gelaufen ist, sollte man jetzt oben beschriebenes Phänomen beobachten können.
# Falls dies aber nicht der Fall sein sollte, dann funktioniert dieses Test-Programm offensichtlich nicht einwandfrei. :(
