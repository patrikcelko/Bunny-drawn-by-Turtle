from PIL import Image
from turtle import (colormode, exitonclick, pencolor, penup, 
                    shape, speed, title, setup, setposition, 
                    tracer, dot, update, bgcolor)

bunny_img = Image.open("./assets/bunny.png", 'r')
data = bunny_img.load()
img_width, img_height = bunny_img.size

shape('turtle')
title("Mergado Bunny")
setup(width=img_width, height=img_height, startx=0, starty=0)
speed(0)
colormode(255)  # We need to suport full RGB
bgcolor((134, 129, 126))
penup()
tracer(False)  # Disable auto-update

for x in range(0, img_width, 3):
    if x % 4 == 0:
        update()
    for y in range(0, img_height, 3):
        r, g, b, _ = data[x,y]  # RGBA
        if (r, g, b) == (0, 0, 0) or (r, g, b) == (197, 194, 191) or \
                (r, g, b) == (166, 163, 160):
            continue
        setposition(x - (img_width // 2), (y - (img_height // 2)) * -1)
        pencolor((r, g, b))
        dot(size=1)

exitonclick()
