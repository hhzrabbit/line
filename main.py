from display import *
from draw import *
import math

screen = new_screen()
red = [ 255, 0, 0 ]
green = [ 0, 255, 0 ]
blue = [ 0, 0, 255 ]
white = [ 255, 255, 255 ]

colors = [red, green, blue, white]

increment = (2 * math.pi) / 360

for i in range(360):
    radius = 150 + i % 20

    angle = i * increment

    if i % 3 == 0:
        color = white
    else:
        color = red
    
    x = int(radius * math.cos(angle)) + 250
    y = int(radius * math.sin(angle)) + 250
    draw_line(screen, 250, 250, x, y, color)
    

display(screen)

save_extension(screen, 'img.png')
