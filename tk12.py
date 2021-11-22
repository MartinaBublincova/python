import tkinter
import random

n = int(input("Zadaj n: "))

canvas = tkinter.Canvas(height=500, width=385)
canvas.pack()

x, y, m = 10, 100, 5
a = (370-n*m)/n
for i in range(0, n):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = f'#{r:02x}{g:02x}{b:02x}'
    canvas.create_rectangle(x, y, x + a, y + a, fill=rgb_color)
    x = x+a+m

tkinter.mainloop()
