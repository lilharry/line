from display import *
import random
def draw_line( screen, x0, y0, x1, y1, color ): 
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)

    color = [r,g,b]
    dx = x1 - x0
    dy = y1 - y0
    
    x = x0  
    y = y0
    
    print("drawing line:\n x0 = %d, y0 = %d\n x1 = %d, y1 = %d\n"%(x0,y0,x1,y1))
    #if vertical
    if dx == 0:
        if y < y1:
            while y < y1:
                plot(screen,color,x,y)
                y+=1
        else:
            draw_line(screen,x1,y1,x0,y0,color)
    
    #if horizontal
    elif dy == 0:
        if x < x1:
            while x < x1:
                plot(screen,color,x,y)
                x+=1
        else:
            draw_line(screen,x1,y1,x0,y0,color)
    #if first octant
    elif dy > 0:
        if dx > 0:
            if dx >= dy:
                d = dy - dx
                while (x < x1):
                    plot(screen, color, x,y)
                    if (d>0):
                        y+=1
                        d-= dx
                    d+=dy
                    x+=1
            #if second octant
            if dy > dx and dx > 0:
                d = dx - dy
                while (y < y1):
                    plot(screen,color,x,y)
                    if (d>0):
                        x+=1
                        d-=dy
                    d+=dx
                    y+=1
        else:
            draw_line(screen,x1,y1,x0,y0,color)
    else:
           
        if dx > 0:
            #if eight octant  
            if dx >= abs(dy):
                d = dy - dx
                
                while (x < x1):
                    plot(screen,color,x,y)
                    if (d>0):
                        y-=1
                        d-=dx
                    d-=dy
                    x+=1
            #if seventh octant
            if abs(dy) > dx:
                d = dx - dy
                #600
                
                #      500 > 0
                while (y > y1):
                    plot(screen,color,x,y)
                    if (d>0):
                        x+=1
                        d+=dy
                    d+=dx
                    y-=1
        else:
            draw_line(screen,x1,y1,x0,y0,color)

        



    