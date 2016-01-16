"""
Ein kleines Zug-Programm für die kleine LED-Stripe-Library.
Wenn alles glatt läuft, müsste ein roter Zug in Endlosschleife hin- und herfahren.

© Elias Gürlich, 2016
"""

from led_stripe_py import LED_Stripe, LED_Stripe_Datagram, LED # Alles aus der LED-Stripe-Lib importieren
import math # Importiere natives Math-Modul
import time # Importiere natives Time-Modul
import random

HOST_NAME = "172.22.99.206"
PORT = 2342

led_stripe = LED_Stripe(HOST_NAME, PORT) # Erzeuge Lichterkette mit diesem Host und Port

leds = []

for i in range(0,20):
    led = LED(0x00, 0x00, 0xff)
    leds.append(led)

for i in range(0,206): 
    led = LED(0x00,0x00,0x00) 
    leds.append(led)

datagram = LED_Stripe_Datagram(priority=0xff, command=0x00, leds=leds)

happy_colors = [
    [0xff, 0x00, 0x00],
    [0x00, 0xff, 0x00],
    [0x00, 0x00, 0xff],
    [0xff, 0xff, 0x00]
]

def randColor():
    randomNum = random.randint(0,len(happy_colors))
    return happy_colors[randomNum-1]

position = 0
train_length = 30
vorwaerts = True
#color = randColor()
while True:
    leds = []
    color = randColor()
    for i in range(0,20):
        if i == (position % 20) or i==20-(position % 20):
            led = LED(color[0], color[1], color[2])
        else:
            led = LED(0x00, 0x00, 0x00)
        leds.append(led)

    for i in range(0, position):
        led = LED(0x00,0x00,0x00)
        leds.append(led)

    for i in range(0,train_length):
        led = LED(0xff-math.ceil(0xff/train_length*i), 0x00, 0x00+math.ceil(0xff/train_length*i))
        leds.append(led)
    
    for i in range(0, 206-(position+train_length)):
        led = LED(0x00, 0x00, 0x00)
        leds.append(led)
    

    datagram = LED_Stripe_Datagram(priority=0xff, command=0x00, leds=leds)
    led_stripe.send(datagram)
    if (206 - train_length == position and vorwaerts) or (position == 0 and not vorwaerts):
        vorwaerts = not vorwaerts

    if vorwaerts:    
        position += 1
    else:
        position -= 1
    
    time.sleep(0.025)

# Wenn alles glatt gelaufen ist, sollte man jetzt oben beschriebenes Phänomen beobachten können.
# Falls dies aber nicht der Fall sein sollte, dann funktioniert dieses Test-Programm offensichtlich nicht einwandfrei. :(
