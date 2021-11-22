import tkinter
import random
canvas = tkinter.Canvas(height=400, width=400)
canvas.pack()

n = 100
ro = 20

for i in range(0, n):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_color = f'#{r:02x}{g:02x}{b:02x}'
    x = random.randint(20, 380)
    y = random.randint(20, 380)
    canvas.create_oval(x-ro, y-ro, x+ro, y+ro, fill=rgb_color)
    value = random.randint(1, 9)
    canvas.create_text(x, y, text=value, font='arial 30')

tkinter.mainloop()
