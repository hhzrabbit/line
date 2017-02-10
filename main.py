from display import *
from draw import *

screen = new_screen()
red = [ 255, 0, 0 ]
green = [ 0, 255, 0 ]
blue = [ 0, 0, 255 ]
white = [ 255, 255, 255 ]

colors = [red, green, blue, white]

draw_line(screen, 0, 300, 200, 500, white)
draw_line(screen, 0, 400, 200, 400, white)

draw_line(screen, 5, 480, 153, 482, white)

for y in range(0, 200, 4):
    draw_line(screen, 0, 00, 250, y, colors[y / 4 % 4]) 

display(screen)

save_extension(screen, 'img.png')
