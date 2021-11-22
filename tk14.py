import tkinter
import random
import math
canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()


a = 280
n = 100
for i in range(0, n):
    a = random.randint(10, 50)
    x = random.randint(10, 480)
    y = random.randint(10, 500)
    v = math.sqrt(a**2-(a/2)**2)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = f'#{r:02x}{g:02x}{b:02x}'
    canvas.create_polygon(x, y, x+a, y, x+a/2, y-v, fill=rgb_color)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = f'#{r:02x}{g:02x}{b:02x}'
    canvas.create_rectangle(x, y, x+a, y+a, fill=rgb_color, outline=rgb_color)


tkinter.mainloop()
