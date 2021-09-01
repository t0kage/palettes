import math
import imagehelper

IMAGE_HEIGHT = 256

#Wir haben zwei Punkte auf der kurve
#P1
XSTART = 40
YSTART = 40

#P2
XSTOP = 90
YSTOP = 90

#Schritt: Um wieviel sich der Farbton h immer aendert
HSTEP = 70

#Groesse der Palette
N = int(input("Wie viele Farben wollen se? "))
IMAGE_WIDTH = IMAGE_HEIGHT * N

#Anfangsfarbton h
HSTART = int(input("Welchen Farbton wollen se? "))


# our functions for calculating the lighness based off of the saturation
#logarithmic curve (CONSTANT) P1(30, 30) P2(100, 80)
def lightness_log(s):
    l = round(11.8 * math.log((s - 29)) + YSTART)
    return l

#lineare funktion, (KONSTANT) geht durch P(30, 30) und P1(100, 80)
def lightness_linear(s):
    l = round((5/7)*s + (60/7))
    return l

#lineare funtion (DYNAMISCH)
#f(x) = mx + n
def lightness_custom(s):
    m = (XSTOP - XSTART) / (YSTOP - YSTART)
    #f(XSTART) = YSTART
    n = YSTART - XSTART * m
    l = round(m * s + n)
    return l

#GIBT DIE NAECHSTE FARBE AUS
def next_h(h):
    h =  (h + HSTEP) % 360
    return h


palette = []
h = HSTART

#RECHNET DIE PALETTENFARBEN UND TUT SIE IN DIE PALETTE
for i in range(N):
    s = i * int((XSTOP - XSTART)/N) + XSTART
    l = lightness_custom(s)
    h = next_h(h)
    palette.append((h, s, l))

imagehelper.draw_image_from_palette(palette=palette, height= IMAGE_HEIGHT)