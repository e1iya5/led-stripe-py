"""
Ein kleines Test-Programm für die kleine LED-Stripe-Library.
Wenn alles glatt läuft, müsste die Lichterkette komplett in rot erleuchten.

© Elias Gürlich, 2016
"""

from led_stripe_py import LED_Stripe, LED_Stripe_Datagram, LED # Alles aus der LED-Stripe-Lib importieren
import math # Importiere natives Math-Modul

HOST_NAME = "172.22.99.206"
PORT = 2342

led_stripe = LED_Stripe(HOST_NAME, PORT) # Erzeuge Lichterkette mit diesem Host und Port

leds = [] # Hier kommen die LEDs rein *-*
for i in range(0,226): #Für 226 LEDs
    led = LED(0xff, 0x00, 0x00) #Setze LED rot
    leds.append(led) 

datagram = LED_Stripe_Datagram(priority=0x01, command=0x00, leds=leds) # Erzeuge Datagram mit Priorität 255, (seeeeehr hoch) Kommando 0 (Setze LED-Farben) und den ganzen LEDs, die wir definiert haben

while True:
    led_stripe.send(datagram) # Sende Datagram an Lichterkette

# Wenn alles glatt gelaufen ist, sollte man jetzt oben beschriebenes Phänomen beobachten können.
# Falls dies aber nicht der Fall sein sollte, dann funktioniert dieses Test-Programm offensichtlich nicht einwandfrei. :(
