import board
import displayio
import terminalio
import time
import random
from adafruit_display_text import label

display = board.DISPLAY
font = terminalio.FONT
group = displayio.Group()

while True:
    bitmap = displayio.Bitmap(display.width, display.height, 2)
    palette = displayio.Palette(2)
    palette[0] = 0x000000
    palette[1] = 0x00FF00
    bitmap_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
    bitmap_grid.x = 0
    bitmap_grid.y = 0

    size = random.randint(20,100)
    posx = random.randint(0,display.width-size)
    posy = random.randint(0,display.height-size)

    for x in range(posx, posx+size):
        for y in range(posy, posy+size):
            bitmap[x, y] = 1

    text = "HELLO WORLD " + str(random.randint(0,250))
    text_grid = label.Label(font, text=text, color=0xFFFFFF)
    text_grid.x = random.randint(10,160)
    text_grid.y = random.randint(10,230) 

    group.append(bitmap_grid)
    group.append(text_grid)
    group.x = 0
    group.y = 0

    display.show(group)
    time.sleep(1)

    group.pop(1)
    group.pop(0)
