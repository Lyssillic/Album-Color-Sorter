
# A quick project I programmed to sort my favorite albums by color hue to create an album wall!

from os import listdir
from os.path import isfile, join
import colorsys
from colorthief import ColorThief
from PIL import Image

def GetDominantColor(album):
    color_thief = ColorThief('albums/' + album)
    print("got color thief")
    dominant_color = color_thief.get_color(quality=1)
    print("got dominant color")
    return dominant_color

def ConvertToHue(rgb):
    (r, g, b) = rgb 
    hsv = colorsys.rgb_to_hsv(r, g, b)
    return hsv[0]

print("Starting")
# Create dictionary and album list
albumColor = {}
albums = [f for f in listdir('albums') if isfile(join('albums', f))]

for album in albums:
    im = Image.open('albums/' + album)
    im.show()

## Loop through each album
#for album in albums:
#    print("Album: " + album)
#    # Get dominant color from album
#    c = GetDominantColor(album)
#    print("got dominant color: " + str(c))

#    # Convert color from HEX to Hue
#    c = ConvertToHue(c)
#    print("got hue: " + str(c))

#    # Insert into dictionary
#    albumColor[album] = c
#    print("added to dictionary")
    
#    print("Done \n")

## Sort dictionary by color (value)
#albumColor = dict(sorted(albumColor.items(), key=lambda item: item[1]))

#print("Sorting done")

## Print list of albums in order of color hue
#for item in albumColor.items():
#    print(item[0])