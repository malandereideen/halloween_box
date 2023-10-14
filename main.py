from machine import Pin
import time
from neopixel import NeoPixel
from dfplayermini import Player
from random import randint




taste1 = Pin(27,Pin.IN,Pin.PULL_UP)
taste2 = Pin(25,Pin.IN,Pin.PULL_UP)
taste3 = Pin(32,Pin.IN,Pin.PULL_UP)

pir = Pin(22,Pin.IN)

pixels = NeoPixel(Pin(18),1)
pixels.fill((0,0,0))
pixels.write()

music = Player(pin_TX=17,pin_RX=16)


def handle_taste1():
    global volume
    print("Taste Volume lauter gedrückt")
    myvol = music.volume()
    music.volume_up()
    music.play(5)
    print(myvol)
    
def handle_taste2():
    global farbe, colr, colg, colb
    print("Taste Color gedrückt")
    if farbe == 9:
        farbe = -1
    farbe = farbe + 1
    pixels.fill((colr[farbe],colg[farbe],colb[farbe]))
    pixels.write()
    time.sleep(1)
    pixels.fill((0,0,0))
    pixels.write()
    
def handle_taste3():
    global volume
    print("Taste Volume leiser gedrückt")
    myvol = music.volume()
    music.volume_down()
    music.play(5)
    print(myvol)
    

def handle_pir():
    global blink
    print("Pir hat ausgelöst")
    rand = randint(1,9)
    print(rand)
    music.play(rand)
    for i in range(15):
        pixels.fill((colr[farbe],colg[farbe],colb[farbe]))
        pixels.write()
        time.sleep(blink)
        pixels.fill((0,0,0))
        pixels.write()
        time.sleep(blink)
    


music.volume(volume)

while True:
    if taste1.value() == 0:
        time.sleep_ms(50)
        if taste1.value() == 0:
            handle_taste1()
            while taste1.value() == 0:
                continue
    if taste2.value() == 0:
        time.sleep_ms(50)
        if taste2.value() == 0:
            handle_taste2()
            while taste2.value() == 0:
                continue
    if taste3.value() == 0:
        time.sleep_ms(50)
        if taste3.value() == 0:
            handle_taste3()
            while taste3.value() == 0:
                continue
    if pir.value():
        handle_pir()
        time.sleep(3)
        
        