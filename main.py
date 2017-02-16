from display import *
from draw import *
import random
screen = new_screen()
color = [ 0, 255, 0 ]
'''
numlines = 500
for i in range(numlines):
    draw_line(screen,
        random.randrange(500),
        random.randrange(500),
        random.randrange(500),
        random.randrange(500),
        color)

'''

draw_line(screen,250,0,250,500,color)
draw_line(screen,0,250,500,250,color)


draw_line(screen,0,0,500,0,color)
draw_line(screen,0,0,500,100,color)
draw_line(screen,0,0,500,200,color)
draw_line(screen,0,0,500,300,color)
draw_line(screen,0,0,500,400,color)
draw_line(screen,0,0,500,500,color)
draw_line(screen,0,0,400,500,color)
draw_line(screen,0,0,300,500,color)
draw_line(screen,0,0,200,500,color)
draw_line(screen,0,0,100,500,color)
draw_line(screen,0,0,0,500,color)

draw_line(screen,0,500,0,0,color)
draw_line(screen,0,500,100,0,color)
draw_line(screen,0,500,200,0,color)
draw_line(screen,0,500,300,0,color)
draw_line(screen,0,500,400,0,color)
draw_line(screen,0,500,500,0,color)
draw_line(screen,0,500,500,100,color)
draw_line(screen,0,500,500,200,color)
draw_line(screen,0,500,500,300,color)
draw_line(screen,0,500,500,400,color)
draw_line(screen,0,500,500,500,color)

draw_line(screen,500,0,0,0,color)
draw_line(screen,500,0,0,100,color)
draw_line(screen,500,0,0,200,color)
draw_line(screen,500,0,0,300,color)
draw_line(screen,500,0,0,400,color)
draw_line(screen,500,0,0,500,color)
draw_line(screen,500,0,100,500,color)
draw_line(screen,500,0,200,500,color)
draw_line(screen,500,0,300,500,color)
draw_line(screen,500,0,400,500,color)
draw_line(screen,500,0,500,500,color)

draw_line(screen,500,500,0,500,color)
draw_line(screen,500,500,0,400,color)
draw_line(screen,500,500,0,300,color)
draw_line(screen,500,500,0,200,color)
draw_line(screen,500,500,0,100,color)
draw_line(screen,500,500,0,0,color)
draw_line(screen,500,500,100,0,color)
draw_line(screen,500,500,200,0,color)
draw_line(screen,500,500,300,0,color)
draw_line(screen,500,500,400,0,color)
draw_line(screen,500,500,500,0,color)

display(screen)
save_extension(screen, 'img.png')
