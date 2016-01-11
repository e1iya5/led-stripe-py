"""
Eine kleine Bibliothek für die LED-Stripe im HQ. (https://wiki.c3d2.de/LED-Stripe)
Damit sollte diese jetzt mit wenig Aufwand programmierbar sein.

© Elias Gürlich, 2016
"""

import socket
from struct import pack

class LED_Stripe: # Lichterkette
    def __init__(self, host, port): # Konstruktor nimmt Host-Name und Port der Lichterkette
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Öffne UDP-Socket
        self.host = host # Merke Host-Name
        self.port = port # Merke Port
    
    def send(self, datagram): # Datagram versenden
        self.socket.sendto(bytes(datagram.getData()), (self.host, self.port)) # Sende Datagram mitels UDP-Socket an Host-Name:Port
    
class LED_Stripe_Datagram: # Datagram
    def __init__(self, priority=0xff, command=0x00, leds=[]): # Konstruktor nimmt Priorität (1 Byte), Kommando (1 Byte; 0 zum Setzen von LED-Farbe) und Array mit LEDs
        self.priority = priority # Merke Priorität
        self.command = command # Merke Kommando
        self.leds = leds # Merke LEDs
    
    def getData(self): # Liefert Daten im richtigen Byte-Format
        led_data = [] # Hier kommen die LED-Daten-Bytes rein
        for led in self.leds: # Für jede LED...
            led_data = led_data + led.getData() # ...füge Bytes der LED zu led_data hinzu.
        
        formattedLen = bytes(pack('i', len(led_data))) # Länge der LED-Bytes in Network Byte Order formatieren
        data = [
            self.priority, # Byte 0: Priorität
            self.command, # Byte 1: Kommando
            formattedLen[1], # Bytes 2 & 3: Länge der folgenden Daten in Network Byte Order
            formattedLen[0]
        ]
        data = data + led_data # Füge LED-Bytes zu Byte-Block hinzu
        return data # Gib Byte-Block zurück

class LED: # Leuchtdiode (LED)
    def __init__(self, r, g, b): # Konstruktor nimmt 8 Bit rot, 8 Bit grün, 8 Bit blau
        self.r = r # Merke Rot-Wert
        self.g = g # Merke Grün-Wert
        self.b = b # Merke Blau-Wert

    def getData(self): # Liefert Daten im richtigen Byte-Format
        data = [ # Ja, BGR ist Absicht, stand so in der Dokumentation... Ô.ô
            self.b, # Byte 0: Blau-Wert
            self.g, # Byte 1: Grün-Wert
            self.r  # Byte 2: Rot-Wert
        ]
        return data
