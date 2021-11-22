import tkinter
import random

my_text = str(input("zadaj text"))

canvas = tkinter.Canvas(height=500, width=5000000)
canvas.pack()

x, y, a, z = 50, 100, 30, 0


for i in range(0, len(my_text)):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = f'#{r:02x}{g:02x}{b:02x}'
    canvas.create_rectangle(x, y, x+a, y+a, fill=rgb_color)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = f'#{r:02x}{g:02x}{b:02x}'
    canvas.create_text(
        x+a/2, y+a/2, text=my_text[z].upper(), fill=rgb_color, font='arial 26')
    z = z+1
    x = x+a

tkinter.mainloop()
