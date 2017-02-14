from display import *

def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0
    
    #if first octant
    d = 2 * dy - dx
    if dx > dy and dy > 0:
        x = x0  
        y = y0
        while (x < x1):
            plot(screen, color, x,y)
            d = x+2,y+1
            if (d>0):
                y+=1
            x+=1

    