from display import *

def getOctant(slope):
    if slope <= -1:
        return 7
    elif slope < 0:
        return 8
    elif slope <= 1:
        return 1
    else:
        return 2

def oct1(x, y, x1, y1, screen, color, A, B, d):

    while x <= x1:
        plot(screen, color, x, y)
        if d > 0:

            y += 1
            d += 2 * B
        x += 1
        d += 2 * A

    
def oct2(x, y, x1, y1, screen, color, A, B, d):
    while y <= y1:
        plot(screen, color, x, y)
        if d < 0:
            x += 1
            d += 2 * A
        y += 1
        d += 2 * B


def oct8(x, y, x1, y1, screen, color, A, B, d):
    while x <= x1:
        plot(screen, color, x, y)
        if d < 0:
            y -= 1
            d -= 2 * B
        x += 1
        d += 2 * A

def oct7(x, y, x1, y1, screen, color, A, B, d):
    while y >= y1:
        plot(screen, color, x, y)
        if d > 0:
            x += 1
            d += 2 * A
        y -= 1
        d -= 2 * B

     
def draw_line(x0, y0, x1, y1, screen, color):

    if x0 > x1:
        draw_line(x1, y1, x0, y0, screen, color)
        
    else:
        
        A = y1 - y0
        B = - (x1 - x0)

        deltaX = (x1 - x0)
        deltaY = (y1 - y0)

        if deltaX == 0:
            if deltaY > 0:
                octant = 2
            else:
                octant = 7
        else:
            slope = deltaY * 1.0 / deltaX
            octant = getOctant(slope)

        if octant == 1: 
            d = 2 * A + B

        elif octant == 2:
            d = 2 * B + A

        elif octant == 8:
            d = 2 * A - B

        else: #7
            d = A - 2 * B

        mapping = {1 : oct1,
                   2 : oct2,
                   7 : oct7,
                   8 : oct8
        }

        mapping[octant](x0, y0, x1, y1, screen, color, A, B, d)
