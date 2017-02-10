from display import *

def draw_line( screen, x0, y0, x1, y1, color ):

    if x0 > x1:
        draw_line(screen, x1, y1, x0, y0, color)
        
    else:
        A = y1 - y0
        B = - x1 - x0
        d = 2 * A + B
    
        x = x0
        y = y0

        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A
    
